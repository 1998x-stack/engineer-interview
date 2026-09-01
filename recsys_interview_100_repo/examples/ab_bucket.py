"""Stable A/B assignment sketch."""
import hashlib


def bucket(user_id: str, experiment_id: str, n: int = 10000) -> int:
    payload = f"{experiment_id}:{user_id}".encode()
    digest = hashlib.sha256(payload).digest()
    return int.from_bytes(digest[:8], "big") % n

if __name__ == "__main__":
    print(bucket("user-42", "rank-v2"))
