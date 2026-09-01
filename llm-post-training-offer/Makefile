.PHONY: check docs serve

check:
	python scripts/validate_questions.py
	python scripts/check_internal_links.py

docs: check
	mkdocs build --strict

serve:
	mkdocs serve
