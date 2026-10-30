"""Translate valid repository-source links for published MkDocs pages.

The source Markdown retains relative links so they work in GitHub's repository
viewer; the published website is built from docs/ and needs external GitHub URLs
for sources/ outside docs/. Only these explicit, known locations are rewritten.
"""
import re

SOURCE_BASE = (
    "https://github.com/1998x-stack/engineer-interview/blob/main/"
    "nlp-llm-interview-100/sources/"
)
SOURCE_LINK = re.compile(
    r"\]\((?:\.\./){1,2}sources/"
    r"(?P<asset>provenance\.md|questions_raw/Q\d{3}\.txt)\)"
)


def on_page_markdown(markdown, page, config, files):
    return SOURCE_LINK.sub(
        lambda match: "](" + SOURCE_BASE + match.group("asset") + ")",
        markdown,
    )
