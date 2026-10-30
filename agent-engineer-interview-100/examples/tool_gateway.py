"""Small, stdlib-only *teaching* gateway for Q023/Q024/Q063/Q081/Q089.

Invariants:
- A model/tool description is never an authorization decision.
- A durable intent is committed BEFORE any external side effect.
- Replaying an operation cannot blindly repeat a side effect.
- Timeout/crash means UNKNOWN until the authoritative resource is reconciled.

The trusted external business API MUST enforce its own authorization and
idempotency when stronger, end-to-end guarantees are required.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Mapping, Any

class AccessDenied(Exception):
    pass

class InvalidRequest(Exception):
    pass

class IdempotencyConflict(Exception):
    pass

class OutcomeUnknown(Exception):
    pass

@dataclass(frozen=True)
class Identity:
    tenant: str
    principal: str

@dataclass(frozen=True)
class Proposal:
    identity: Identity
    tool: str
    args: Mapping[str, Any]
    operation_id: str
    approval_id: str | None = None

@dataclass(frozen=True)
class Tool:
    """handler(operation_id, args) -> JSON-serializable business result.

    Handler represents a trusted API adapter, not executable text from a model.
    Side-effectful adapters should transmit operation_id to the business API.
    """
    handler: Callable[[str, Mapping[str, Any]], Any]
    side_effect: bool = True
    requires_approval: bool = False


class ToolGateway:
    def __init__(
        self,
        database: str | Path,
        tools: Mapping[str, Tool],
        capabilities: Mapping[tuple[str, str], frozenset[str]],
        approvals: Mapping[tuple[str, str, str, str], str] | None = None,
    ):
        self.database = str(database)
        self.tools = dict(tools)
        self.capabilities = dict(capabilities)
        # In production approvals must come from a verified trusted approval service.
        self.approvals = dict(approvals or {})
        with sqlite3.connect(self.database) as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS operations(
                    tenant TEXT NOT NULL, principal TEXT NOT NULL,
                    operation_id TEXT NOT NULL, tool TEXT NOT NULL,
                    request_hash TEXT NOT NULL, status TEXT NOT NULL,
                    result_json TEXT,
                    PRIMARY KEY(tenant, principal, operation_id)
                )
            """)

    def _digest(self, proposal: Proposal) -> str:
        if (not isinstance(proposal.args, Mapping) or
                any(not isinstance(x, str) for x in proposal.args.keys())):
            raise InvalidRequest("tool arguments must be a string-keyed mapping")
        try:
            encoded = json.dumps(
                {"tool": proposal.tool, "args": proposal.args},
                ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
            ).encode("utf-8")
        except (TypeError, ValueError) as exc:
            raise InvalidRequest("tool arguments must be finite JSON values") from exc
        return hashlib.sha256(encoded).hexdigest()

    def _authorize(self, proposal: Proposal) -> Tool:
        if (not isinstance(proposal.identity, Identity) or
                not isinstance(proposal.identity.tenant, str) or
                not isinstance(proposal.identity.principal, str) or
                not proposal.identity.tenant or not proposal.identity.principal or
                not isinstance(proposal.operation_id, str) or
                not proposal.operation_id.strip() or
                not isinstance(proposal.tool, str)):
            raise InvalidRequest("identity, tool and operation_id are required")
        tool = self.tools.get(proposal.tool)
        scopes = self.capabilities.get(
            (proposal.identity.tenant, proposal.identity.principal), frozenset()
        )
        if tool is None or proposal.tool not in scopes:
            raise AccessDenied("tool not permitted for this authenticated principal")
        if tool.requires_approval:
            key = (
                proposal.identity.tenant, proposal.identity.principal,
                proposal.tool, proposal.operation_id
            )
            approved = self.approvals.get(key)
            if not approved or approved != proposal.approval_id:
                raise AccessDenied("independent approval is required")
        return tool

    def _row(self, db: sqlite3.Connection, proposal: Proposal):
        return db.execute(
            "SELECT tool, request_hash, status, result_json FROM operations "
            "WHERE tenant=? AND principal=? AND operation_id=?",
            (proposal.identity.tenant, proposal.identity.principal, proposal.operation_id),
        ).fetchone()

    def run(self, proposal: Proposal) -> Any:
        tool = self._authorize(proposal)
        fingerprint = self._digest(proposal)
        # BEGIN IMMEDIATE serializes local reservations across gateway instances.
        with sqlite3.connect(self.database, timeout=5.0) as db:
            db.execute("BEGIN IMMEDIATE")
            row = self._row(db, proposal)
            if row:
                existing_tool, existing_hash, status, raw = row
                if existing_tool != proposal.tool or existing_hash != fingerprint:
                    raise IdempotencyConflict("operation_id reused for different request")
                if status == "SUCCEEDED":
                    return json.loads(raw)
                # A worker may have crashed between the durable intent and response.
                # Even IN_FLIGHT is ambiguous; never automatically call the tool again.
                raise OutcomeUnknown(f"operation {proposal.operation_id} is {status}")
            db.execute(
                "INSERT INTO operations VALUES (?,?,?,?,?,?,?)",
                (proposal.identity.tenant, proposal.identity.principal,
                 proposal.operation_id, proposal.tool, fingerprint, "IN_FLIGHT", None),
            )

        try:
            result = tool.handler(proposal.operation_id, proposal.args)
            result_json = json.dumps(result, allow_nan=False, ensure_ascii=False)
        except Exception as exc:
            # External systems may have committed before a timeout/error.
            with sqlite3.connect(self.database) as db:
                db.execute(
                    "UPDATE operations SET status='UNKNOWN' WHERE tenant=? AND principal=? "
                    "AND operation_id=? AND status='IN_FLIGHT'",
                    (proposal.identity.tenant, proposal.identity.principal, proposal.operation_id),
                )
            raise OutcomeUnknown("tool outcome unconfirmed; reconcile before continuing") from exc

        # Crash in this window leaves IN_FLIGHT. Replays fail closed.
        with sqlite3.connect(self.database) as db:
            db.execute(
                "UPDATE operations SET status='SUCCEEDED', result_json=? "
                "WHERE tenant=? AND principal=? AND operation_id=? AND status='IN_FLIGHT'",
                (result_json, proposal.identity.tenant, proposal.identity.principal,
                 proposal.operation_id),
            )
        return result

    def reconcile_committed(
        self,
        proposal: Proposal,
        lookup: Callable[[str], Any | None],
    ) -> Any:
        """Confirm remote success by querying the authoritative API by operation_id.

        A None result is *not* proof that no side effect occurred (eventual
        consistency). It leaves the local state UNKNOWN and forbids replay.
        """
        self._authorize(proposal)
        fingerprint = self._digest(proposal)
        with sqlite3.connect(self.database) as db:
            row = self._row(db, proposal)
        if row is None:
            raise InvalidRequest("unknown operation_id; no durable intent")
        if row[0] != proposal.tool or row[1] != fingerprint:
            raise IdempotencyConflict("cannot reconcile a different request")
        if row[2] == "SUCCEEDED":
            return json.loads(row[3])
        try:
            result = lookup(proposal.operation_id)
        except Exception as exc:
            raise OutcomeUnknown("authoritative lookup failed") from exc
        if result is None:
            raise OutcomeUnknown("remote success not confirmed; do not replay")
        try:
            encoded = json.dumps(result, ensure_ascii=False, allow_nan=False)
        except (TypeError, ValueError) as exc:
            raise InvalidRequest("remote result must be JSON-serializable") from exc
        with sqlite3.connect(self.database, timeout=5.0) as db:
            db.execute("BEGIN IMMEDIATE")
            current = self._row(db, proposal)
            if current[2] == "SUCCEEDED":
                return json.loads(current[3])
            db.execute(
                "UPDATE operations SET status='SUCCEEDED', result_json=? "
                "WHERE tenant=? AND principal=? AND operation_id=?",
                (encoded, proposal.identity.tenant, proposal.identity.principal,
                 proposal.operation_id),
            )
        return result

    def status(self, proposal: Proposal) -> str | None:
        """Read status without executing; still requires current authorization."""
        self._authorize(proposal)
        self._digest(proposal)
        with sqlite3.connect(self.database) as db:
            row = self._row(db, proposal)
        return row[2] if row else None
