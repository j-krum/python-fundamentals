# test_number_compressor.py
"""Tests for number_comrpessor."""

import pytest
from number_compressor import number_compressor


class TestNumberCompressor:

    def test_valid_input(self):
        assert number_compressor(1, 2, 3) == 123
        assert number_compressor(0, 0, 0) == 0

    def test_raises_on_float(self):
        with pytest.raises(ValueError):
            number_compressor(1.5, 2, 3)

    def test_raises_on_multi_digit(self):
        with pytest.raises(ValueError):
            number_compressor(10, 2, 3)

    def test_raises_on_negative(self):
        with pytest.raises(ValueError):
            number_compressor(-1, 1, 3)
