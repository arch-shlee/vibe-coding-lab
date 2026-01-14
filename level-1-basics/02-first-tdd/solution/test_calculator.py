"""
계산기 테스트 모듈 - TDD 방식으로 작성

각 테스트는 Red-Green-Refactor 사이클을 거쳐 작성되었습니다.
"""

import pytest
from calculator import add, subtract, multiply, divide, power, modulo


# ==================== 덧셈 테스트 ====================

def test_add_two_positive_numbers():
    """두 양수를 더하는 테스트"""
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """음수 덧셈 테스트"""
    assert add(-5, -3) == -8
    assert add(-5, 3) == -2
    assert add(5, -3) == 2


def test_add_floats():
    """소수점 덧셈 테스트"""
    result = add(0.1, 0.2)
    # 부동소수점 오차 고려
    assert abs(result - 0.3) < 0.0001


def test_add_zero():
    """0과의 덧셈"""
    assert add(5, 0) == 5
    assert add(0, 5) == 5
    assert add(0, 0) == 0


# ==================== 뺄셈 테스트 ====================

def test_subtract_two_numbers():
    """두 숫자를 빼는 테스트"""
    result = subtract(5, 3)
    assert result == 2


def test_subtract_negative_numbers():
    """음수 뺄셈 테스트"""
    assert subtract(-5, -3) == -2
    assert subtract(5, -3) == 8
    assert subtract(-5, 3) == -8


def test_subtract_larger_from_smaller():
    """큰 수에서 작은 수 빼기"""
    assert subtract(3, 5) == -2


def test_subtract_zero():
    """0 빼기"""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5


# ==================== 곱셈 테스트 ====================

def test_multiply_two_numbers():
    """두 숫자를 곱하는 테스트"""
    result = multiply(4, 3)
    assert result == 12


def test_multiply_negative_numbers():
    """음수 곱셈 테스트"""
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(2, -3) == -6


def test_multiply_by_zero():
    """0과의 곱셈"""
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0


def test_multiply_by_one():
    """1과의 곱셈"""
    assert multiply(5, 1) == 5
    assert multiply(1, 5) == 5


# ==================== 나눗셈 테스트 ====================

def test_divide_two_numbers():
    """두 숫자를 나누는 테스트"""
    result = divide(10, 2)
    assert result == 5.0


def test_divide_by_zero():
    """0으로 나누면 예외 발생"""
    with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
        divide(10, 0)


def test_divide_negative_numbers():
    """음수 나눗셈"""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_results_in_float():
    """나눗셈 결과는 항상 float"""
    result = divide(7, 2)
    assert result == 3.5
    assert isinstance(result, float)


# ==================== 추가 함수 테스트 ====================

def test_power():
    """거듭제곱 테스트"""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(2, -1) == 0.5


def test_modulo():
    """나머지 연산 테스트"""
    assert modulo(10, 3) == 1
    assert modulo(7, 2) == 1
    assert modulo(10, 5) == 0


def test_modulo_by_zero():
    """0으로 나머지 연산 시 예외"""
    with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
        modulo(10, 0)


# ==================== 통합 테스트 ====================

def test_calculator_operations_chain():
    """여러 연산을 연쇄적으로 수행"""
    # (10 + 5) * 2 - 10 / 2
    result = add(10, 5)  # 15
    result = multiply(result, 2)  # 30
    result = subtract(result, divide(10, 2))  # 30 - 5 = 25
    assert result == 25


def test_all_operations_with_same_numbers():
    """같은 숫자로 모든 연산 테스트"""
    a, b = 10, 2
    assert add(a, b) == 12
    assert subtract(a, b) == 8
    assert multiply(a, b) == 20
    assert divide(a, b) == 5.0


# ==================== Edge Cases ====================

class TestEdgeCases:
    """극단적인 경우 테스트"""

    def test_very_large_numbers(self):
        """매우 큰 숫자"""
        large = 10**100
        assert add(large, large) == 2 * large

    def test_very_small_numbers(self):
        """매우 작은 숫자"""
        small = 10**-100
        assert add(small, small) == 2 * small

    def test_negative_zero(self):
        """음의 0"""
        assert add(0, -0) == 0
        assert subtract(0, -0) == 0
