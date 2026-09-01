.PHONY: qa docs serve

qa:
	python scripts/qa_repo.py
	python -m compileall -q examples
	@for f in examples/*.py; do python "$$f" >/dev/null; done

docs:
	mkdocs build --strict

serve:
	mkdocs serve
