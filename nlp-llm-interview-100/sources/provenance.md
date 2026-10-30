# Provenance

## Source baseline

- Original source PDF path: `assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf` (**not distributed in this Git snapshot**)
- Extracted text: `sources/pdf_text.txt`
- Per-question raw extraction: `sources/questions_raw/Q001.txt` ... `Q100.txt`

## Transformation policy

1. Preserve question numbering and titles.
2. Preserve the PDF's central answer, Know-Why, pitfalls and follow-up direction where extractable.
3. Add clearly educational expansions: derivation, boundary conditions, engineering notes, implementation checklist and references.
4. Do not claim unverified company-internal provenance.

## Reproducibility boundary (2026-10-30)

The current Git tree does not include the original PDF. It **does** contain `sources/pdf_text.txt` and `sources/questions_raw/Q001.txt` … `Q100.txt`; these can be checked for file presence and linked to the corresponding question IDs. File presence does not prove that extracted text accurately reproduces an unavailable PDF. Do not publish or upload an unlicensed third-party copy. The updated Markdown references this tracked note rather than a missing PDF download.

Run `python scripts/check_repo.py` for the complete Markdown/metadata/source integrity gate; `--require-pdf` is available only for local provenance review where the PDF has been legally obtained.
