"""
계산기 모듈 - TDD로 구현

Red-Green-Refactor 사이클을 통해 개발된 계산기 함수들입니다.
"""


def add(a: float, b: float) -> float:
    """
    두 숫자를 더합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        두 숫자의 합

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0.1, 0.2)
        0.30000000000000004
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    첫 번째 숫자에서 두 번째 숫자를 뺍니다.

    Args:
        a: 첫 번째 숫자 (피감수)
        b: 두 번째 숫자 (감수)

    Returns:
        a - b의 결과

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
        >>> subtract(-5, -3)
        -2
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    두 숫자를 곱합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        두 숫자의 곱

    Examples:
        >>> multiply(4, 3)
        12
        >>> multiply(-2, 3)
        -6
        >>> multiply(0, 100)
        0
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    첫 번째 숫자를 두 번째 숫자로 나눕니다.

    Args:
        a: 첫 번째 숫자 (피제수)
        b: 두 번째 숫자 (제수)

    Returns:
        a / b의 결과

    Raises:
        ValueError: b가 0일 때

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: 0으로 나눌 수 없습니다
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b


# 추가 유틸리티 함수들

def power(base: float, exponent: float) -> float:
    """
    거듭제곱을 계산합니다.

    Args:
        base: 밑
        exponent: 지수

    Returns:
        base ^ exponent의 결과

    Examples:
        >>> power(2, 3)
        8.0
        >>> power(5, 2)
        25.0
    """
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """
    나머지를 계산합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        a를 b로 나눈 나머지

    Raises:
        ValueError: b가 0일 때

    Examples:
        >>> modulo(10, 3)
        1.0
        >>> modulo(7, 2)
        1.0
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a % b
