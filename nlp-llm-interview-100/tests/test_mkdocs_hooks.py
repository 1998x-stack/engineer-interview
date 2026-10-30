from scripts.mkdocs_hooks import SOURCE_BASE, on_page_markdown


def render(text):
    return on_page_markdown(text, None, None, None)


def test_published_links_to_tracked_source():
    original = (
        "[raw](../../sources/questions_raw/Q097.txt) and "
        "[provenance](../../sources/provenance.md)"
    )
    result = render(original)
    assert f"[raw]({SOURCE_BASE}questions_raw/Q097.txt)" in result
    assert f"[provenance]({SOURCE_BASE}provenance.md)" in result
    assert "../../sources/" not in result


def test_homepage_provenance_and_ordinary_links():
    original = "[p](../sources/provenance.md) [q](../04-transformer/Q098.md)"
    result = render(original)
    assert f"[p]({SOURCE_BASE}provenance.md)" in result
    assert "[q](../04-transformer/Q098.md)" in result


def test_unrecognized_sources_are_not_rewritten():
    original = "[x](../../sources/secrets.txt) [link](https://example.com/a)"
    assert render(original) == original
