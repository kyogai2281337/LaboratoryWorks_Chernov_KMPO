import pytest
from main import sum, multiplying, substraction, expo

class TestFunctionsFromModule:
    test_sum_data = [(1, 2, 3), (2, 3, 5), (-3, 4, 1)]
    test_mult_data = [(1, 2, 2), (2, 3, 6), (-3, 4, -12)]
    test_substr_data = [(1, 2, -1), (2, 3, -1), (-3, 4, -7)]
    test_expo_data = [(1, 100, 1), (2, 3, 8), (-3, 4, 81)]

    @pytest.mark.parametrize("a, b, expected", test_sum_data)
    def test_sum(self, a, b, expected):
        assert sum(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", test_mult_data)
    def test_mult(self, a, b, expected):
        assert multiplying(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", test_substr_data)
    def test_substr(self, a, b, expected):
        assert substraction(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", test_expo_data)
    def test_expo(self, a, b, expected):
        assert expo(a, b) == expected
    