"""
계산기 모듈

문자열 수식을 계산하는 고급 계산기입니다.
TDD로 단계적으로 구현되었습니다.
"""
from typing import List, Union
import re


def calculate(expression: str) -> Union[int, float]:
    """
    문자열 수식을 계산합니다.

    Args:
        expression: 계산할 수식 문자열
            예: "2 + 3", "10 - 4 * 2", "(2 + 3) * 4"

    Returns:
        계산 결과 (int 또는 float)

    Raises:
        ValueError: 잘못된 수식인 경우
        ZeroDivisionError: 0으로 나누는 경우

    Examples:
        >>> calculate("2 + 3")
        5
        >>> calculate("10 - 4")
        6
        >>> calculate("2 + 3 * 4")
        14
        >>> calculate("(2 + 3) * 4")
        20
    """
    if not expression or not expression.strip():
        raise ValueError("Expression cannot be empty")

    # 괄호 처리 (재귀)
    expression = _handle_parentheses(expression)

    # 토큰화
    tokens = _tokenize(expression)

    # 입력 검증
    _validate_tokens(tokens)

    # 연산자 우선순위 적용
    # 1. 곱셈, 나눗셈 먼저
    tokens = _apply_high_priority_operations(tokens)

    # 2. 덧셈, 뺄셈
    result = _apply_low_priority_operations(tokens)

    return result


def _handle_parentheses(expression: str) -> str:
    """
    괄호를 재귀적으로 처리합니다.

    가장 안쪽 괄호부터 계산하여 결과로 교체합니다.

    Args:
        expression: 수식 문자열

    Returns:
        괄호가 모두 계산된 수식 문자열
    """
    # 가장 안쪽 괄호 찾기 (정규표현식 사용)
    pattern = r'\(([^()]+)\)'
    match = re.search(pattern, expression)

    if not match:
        # 더 이상 괄호가 없음
        return expression

    # 괄호 안 수식 계산
    inner_expr = match.group(1)
    inner_result = calculate(inner_expr)  # 재귀 호출

    # 결과로 교체
    new_expression = expression[:match.start()] + str(inner_result) + expression[match.end():]

    # 나머지 괄호 처리
    return _handle_parentheses(new_expression)


def _tokenize(expression: str) -> List[str]:
    """
    수식 문자열을 토큰 리스트로 변환합니다.

    Args:
        expression: 수식 문자열

    Returns:
        토큰 리스트 (숫자와 연산자)

    Examples:
        >>> _tokenize("2 + 3")
        ['2', '+', '3']
        >>> _tokenize("10-4*2")
        ['10', '-', '4', '*', '2']
    """
    # 공백 제거
    expression = expression.replace(' ', '')

    # 숫자와 연산자를 분리하는 정규표현식
    # 음수도 지원하기 위해 복잡한 패턴 사용
    pattern = r'(\d+\.?\d*|[\+\-\*/])'
    tokens = re.findall(pattern, expression)

    return tokens


def _validate_tokens(tokens: List[str]) -> None:
    """
    토큰 리스트가 유효한지 검증합니다.

    Args:
        tokens: 토큰 리스트

    Raises:
        ValueError: 유효하지 않은 토큰이 있는 경우
    """
    if not tokens:
        raise ValueError("Invalid expression: no tokens")

    # 숫자와 연산자가 번갈아 나와야 함
    for i, token in enumerate(tokens):
        if i % 2 == 0:  # 짝수 인덱스: 숫자여야 함
            try:
                float(token)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
        else:  # 홀수 인덱스: 연산자여야 함
            if token not in ['+', '-', '*', '/']:
                raise ValueError(f"Invalid operator: {token}")

    # 마지막이 숫자로 끝나야 함
    if len(tokens) % 2 == 0:
        raise ValueError("Invalid expression: ends with operator")


def _apply_high_priority_operations(tokens: List[str]) -> List[str]:
    """
    우선순위가 높은 연산(곱셈, 나눗셈)을 먼저 처리합니다.

    Args:
        tokens: 토큰 리스트

    Returns:
        곱셈, 나눗셈이 처리된 토큰 리스트
    """
    i = 0
    while i < len(tokens):
        if i > 0 and tokens[i] in ['*', '/']:
            # 이전 숫자, 연산자, 다음 숫자를 계산
            left = float(tokens[i - 1])
            operator = tokens[i]
            right = float(tokens[i + 1])

            if operator == '*':
                result = left * right
            else:  # operator == '/'
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result = left / right

            # 결과로 교체
            tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
            # 인덱스 조정 (결과가 이전 숫자 위치에)
            i = i - 1
        else:
            i += 1

    return tokens


def _apply_low_priority_operations(tokens: List[str]) -> Union[int, float]:
    """
    우선순위가 낮은 연산(덧셈, 뺄셈)을 처리합니다.

    Args:
        tokens: 토큰 리스트

    Returns:
        최종 계산 결과
    """
    if len(tokens) == 1:
        result = float(tokens[0])
        # 정수로 표현 가능하면 정수로
        return int(result) if result.is_integer() else result

    # 왼쪽부터 순서대로 계산
    result = float(tokens[0])

    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = float(tokens[i + 1])

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand

        i += 2

    # 정수로 표현 가능하면 정수로
    return int(result) if result.is_integer() else result
