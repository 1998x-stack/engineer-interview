"""CLI regression checks against the tracked 100-question dataset."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/random_interview.py"


def run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT, text=True, capture_output=True, check=False
    )


def test_seed_reproducible():
    first = run("--count", "4", "--seed", "42")
    second = run("--count", "4", "--seed", "42")
    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout
    assert sum(line.startswith("Q") and " | " in line for line in first.stdout.splitlines()) == 4


def test_zero_or_negative_count_fails_with_useful_error():
    for n in ("0", "-3"):
        result = run("--count", n)
        assert result.returncode != 0
        assert "positive integer" in result.stderr


def test_empty_filter_fails_instead_of_silent_success():
    result = run("--frequency", "not-a-frequency")
    assert result.returncode != 0
    assert "no interview questions match" in result.stderr


def test_chapter_and_priority_filter():
    result = run("--chapter", "3", "--priority20", "--count", "20", "--seed", "1")
    assert result.returncode == 0
    assert "Tool Calling" in result.stdout
    assert "q000" not in result.stdout.lower()
