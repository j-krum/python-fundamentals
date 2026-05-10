# test_is_prime.py
"""Tests for the module is_prime."""

from is_prime import is_prime


class TestIsPrime:
    """Tests for the is_prime function"""

    def test_is_prime_float(self):
        """The number is not an integer, ISN'T prime."""
        assert is_prime(1.5) is False  # type: ignore
        assert is_prime(2.5) is False  # type: ignore

    def test_is_prime_negatives(self):
        """The number is negative, ISN'T prime"""
        assert is_prime(-1) is False
        assert is_prime(-10) is False

    def test_is_prime_zero(self):
        """Tests if 0 is a prime, it ISN'T"""
        assert is_prime(0) is False

    def test_is_prime_one(self):
        """Tests if the number 1 is prime, it ISN'T"""
        assert is_prime(1) is False

    def test_positive_numbers_from_2_to_10(self):
        """Test numbers from 2 to 10."""
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(4) is False
        assert is_prime(5) is True
        assert is_prime(6) is False
        assert is_prime(7) is True
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False

    def test_letters_and_special_characters(self):
        assert is_prime("String with Sp&c|4L@$#%") is False  # type: ignore
