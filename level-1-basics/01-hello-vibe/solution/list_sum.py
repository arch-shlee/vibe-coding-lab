"""
리스트 합산 프로그램

숫자 리스트의 모든 요소를 합산하는 함수를 구현합니다.
"""

def sum_list(numbers):
    """
    숫자 리스트의 모든 요소를 합산합니다.

    Args:
        numbers: 숫자들의 리스트

    Returns:
        리스트의 모든 숫자의 합
    """
    total = 0
    for num in numbers:
        total += num
    return total


# 대체 구현 (Python 내장 함수 사용)
def sum_list_builtin(numbers):
    """
    Python의 내장 sum 함수를 사용한 구현

    Args:
        numbers: 숫자들의 리스트

    Returns:
        리스트의 모든 숫자의 합
    """
    return sum(numbers)


# 함수 테스트
if __name__ == "__main__":
    # 예제 1
    numbers1 = [1, 2, 3, 4, 5]
    result1 = sum_list(numbers1)
    print(f"리스트 {numbers1}의 합: {result1}")

    # 예제 2
    numbers2 = [10, 20, 30, 40]
    result2 = sum_list(numbers2)
    print(f"리스트 {numbers2}의 합: {result2}")

    # 내장 함수 비교
    result3 = sum_list_builtin(numbers1)
    print(f"내장 함수 사용: {result3}")

    # 빈 리스트
    empty_list = []
    result4 = sum_list(empty_list)
    print(f"빈 리스트의 합: {result4}")
