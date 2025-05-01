"""Testing main.py."""

from main import estimate_count


def test_mushroom_count_returns_int():
    """Checks if func output is int"""
    assert isinstance(estimate_count(), int)
