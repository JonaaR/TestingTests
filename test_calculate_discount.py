import unittest

import pytest

from calculate_discount import calculate_discount

#was ist das für ein klasse, attribute?
class TestCalculateDiscount(unittest.TestCase):

    def test_calculate_discount_1(self):
        expected = 0
        amount = 1
        member = False

        result = calculate_discount(amount, member)

        assert result == expected


    def test_calculate_discount_3(self):
        expected = 1 / 4
        amount = 3
        member = False

        result = calculate_discount(amount, member)

        assert result == expected


    def test_calculate_discount_4(self):
        expected = 1 / 3
        amount = 4
        member = False

        result = calculate_discount(amount, member)

        assert result == pytest.approx(expected, rel=1e-3)


    def test_calculate_discount_5(self):
        expected = 1 / 3
        amount = 5
        member = False

        result = calculate_discount(amount, member)

        assert result == pytest.approx(expected, rel=1e-3)

    def test_calculate_discount_6(self):
        expected = 1 /2
        amount = 6
        member = False

        result = calculate_discount(amount, member)

        assert result == pytest.approx(expected, rel=1e-3)

    def test_calculate_discount_10(self):
        expected = 1 / 2
        amount = 10
        member = False

        result = calculate_discount(amount, member)

        assert result == pytest.approx(expected, rel=1e-3)