# Repository Manifest

- Repository: `web-security-interview-100`
- Build date: 2026-09-02
- Question Markdown files: **100**
- Chapters: **10**
- Source PDF pages: **209**
- Source PDF SHA-256: `72551f37e1e84003067496822ea730fb00747e609395b4fdc287edd3d7424834`
- Review checklists: **6**
- Documentation guides/mappings: **11**

## Content model

Each question contains:

1. PDF-derived master answer with source page.
2. GitHub enhanced deep-dive.
3. Security invariants.
4. Code-review / design-review / testing checklist.
5. Additional gotchas and senior follow-up questions.
6. Standard mappings and related-question navigation.
7. V2 professional enrichment: threat model, failure chain, architecture placement and verification matrix.
8. 30-second / 2-minute / 5-minute interview answer levels and senior-level trade-offs.

Run `python scripts/validate_repo.py` to validate repository completeness and local links.


## V2 professional enrichment

- All **100/100** question files contain the V2 AppSec-engineering section.
- Automated quality gate: `python scripts/content_quality.py`.
- Repository validation now checks V2 headings and a minimum enriched content size.
