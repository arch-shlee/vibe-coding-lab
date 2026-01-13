"""
간단한 계산기 프로그램

두 숫자를 더하는 add 함수를 구현합니다.
"""

def add(a, b):
    """
    두 숫자를 더합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        두 숫자의 합
    """
    return a + b


# 함수 테스트
if __name__ == "__main__":
    result = add(3, 5)
    print(f"3 + 5 = {result}")

    result = add(10, 20)
    print(f"10 + 20 = {result}")

    # 사용자 입력받아 계산
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
