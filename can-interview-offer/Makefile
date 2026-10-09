.PHONY: validate book pdf examples clean

validate:
	python scripts/build_book.py
	python scripts/validate_repo.py
	python -m py_compile examples/python/*.py examples/testing/*.py scripts/*.py

book:
	python scripts/build_book.py

pdf:
	bash scripts/build_pdf.sh

examples:
	python examples/python/encode_decode.py

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
