.PHONY: validate index interview

validate:
	python scripts/validate_repo.py
	python scripts/build_index.py --check
	python scripts/check_links.py

index:
	python scripts/build_index.py

interview:
	python scripts/random_interview.py --count 5

