from pathlib import Path

def test_100_question_markdowns():
    root=Path(__file__).resolve().parents[1]
    assert len(list((root/'docs').glob('*/q[0-9][0-9][0-9]-*.md')))==100
