.PHONY: check test docs
check:
	python scripts/check_repo.py
	python scripts/build_index.py --check
	python scripts/check_contracts.py

docs:
	python scripts/stage_docs.py
	mkdocs serve

test:
	python -m pytest -q tests
