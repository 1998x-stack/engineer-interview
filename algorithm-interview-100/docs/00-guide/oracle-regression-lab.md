# M06 · Algorithm Oracle & Complexity Lab

This GitHub-only extension preserves the existing 100 stable LeetCode question IDs.

## What is now executable

- `tests/test_smoke.py`: original ten single-example smoke tests.
- `tests/test_differential.py`: 31 independent, seeded problem families using brute-force, reference-library or state-machine oracles. This checks normal LeetCode input constraints, not just one hand-picked example.
- `tests/test_contract_edges.py`: explicit rejection of invalid empty streams, empty array median, invalid weighted sampling and invalid partition-count inputs.
- `scripts/check_contracts.py`: registry/frontmatter identity, physical file sets, and *exact* correspondence of Section 9 inline Python snippets to their standalone `solutions/python/*.py` source.
- `.github/workflows/algorithm-interview.yml`: root-level CI that GitHub recognizes in the parent monorepo.

From `algorithm-interview-100/`:

```bash
python scripts/check_repo.py
python scripts/check_content_depth.py
python scripts/check_contracts.py
python -m unittest discover -s tests -v
```

The suite uses the Python standard library (Python 3.12 in GitHub CI), deterministic seeds and small bounded inputs. No external APIs, GPU, third-party packages or nondeterministic success thresholds.

## Contracts and correctness boundaries

- **LC4**: median is undefined when *both* sorted arrays are empty; raise `ValueError`. The original judge supplies at least one element.
- **LC295**: median before the first insertion is undefined; raise `ValueError`.
- **LC528**: weights must be nonempty *positive integers*; anything else raises `ValueError`, rather than failing in random sampling or silently returning an invalid probability.
- **LC698**: `k` must be between 1 and `n`, values must be positive integers; inputs are sorted into a new list so a reusable API does not surprise the caller by mutating their array.
- **Randomized selection**: LC528 is checked by *exhaustively mapping random tickets to the intervals*; it does not rely on statistical randomness. LC470 rejection sampling is checked by enumerating the 49 initial rand7 pairs.
- **QuickSelect**: the LC215 implementation uses randomized pivoting. It has expected linear time under independent uniform pivot assumptions, **not** a worst-case linear-time bound.
- **Backtracking**: LC698 remains worst-case exponential, and the sort adds `O(n log n)` preprocessing. Runtime claims cannot simply be equated with a typical benchmark case.
- **LeetCode assumptions**: cases such as LC45 unreachable last index, LC209 nonpositive input and other out-of-domain inputs are not silently treated as guaranteed-supported; extending APIs requires a separate, explicit contract.

## Verification limits

Random differential tests are *not* a formal proof and do not verify all 100 algorithms, very large inputs, adversarial hash worst cases, concurrency, or external LeetCode judge acceptance. They do find regressions in the covered algorithms and reproduce with a fixed seed. Continue adding per-family oracles and complexity benchmarks in follow-up modules; do not infer untested cases are correct.

The original frozen PDF/DOCX live under `docs/assets/` and are *not* modified. The tests check the current Python/Markdown teaching materials rather than claiming that original PDF claims have been independently re-audited.
