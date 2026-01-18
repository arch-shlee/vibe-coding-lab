"""
계산기 모듈

문자열 수식을 계산하는 고급 계산기입니다.
TDD로 단계적으로 구현해보세요.
"""


def calculate(expression: str):
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
    """
    # TODO: 여기에 계산기를 구현하세요!
    # 힌트: TDD 사이클을 따라 단계적으로 구현하세요.
    pass


# TODO: 필요한 헬퍼 함수들을 추가하세요.
# 예:
# - tokenize(expression): 문자열을 토큰 리스트로 변환
# - apply_operations(tokens): 연산 수행
# - handle_parentheses(expression): 괄호 처리
# 등등...
