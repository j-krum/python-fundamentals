# test_year_validator.py
"""Tests for the module year_validator."""

from year_validator import is_leap_year


class TestIsLeapYear:
    """Tests for the is_leap_year function."""

    def test_year_divisible_by400_is_leap(self):
        """Years divisible by 400 ARE leap years."""
        assert is_leap_year(2000) is True
        assert is_leap_year(1600) is True

    def test_year_divisible_by_100_not_leap(self):
        """Years divisible by 100 (but not by 400)
        ARE NOT leap years."""
        assert is_leap_year(1900) is False
        assert is_leap_year(2100) is False

    def test_year_divisible_by_4_is_leap(self):
        """Years divisible by 4 (but not by 100)
        ARE leap years."""
        assert is_leap_year(2024) is True
        assert is_leap_year(2020) is True

    def test_year_not_divisible_by_4_not_leap(self):
        """Years NOT divisible by 4
        ARE NOT leap years."""
        assert is_leap_year(2023) is False
        assert is_leap_year(2021) is False
