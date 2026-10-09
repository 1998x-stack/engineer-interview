.PHONY: validate stats

validate:
	python scripts/validate_repo.py

stats:
	@echo "Question files:" $$(find questions -type f -name 'Q*.md' | wc -l)
	@echo "Markdown files:" $$(find . -type f -name '*.md' | wc -l)
