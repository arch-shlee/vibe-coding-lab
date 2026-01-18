"""
계산기 테스트

TDD의 Red-Green-Refactor 사이클을 따라 작성된 완전한 테스트 스위트입니다.
"""
import pytest
from calculator import calculate


# ========== Phase 1: 기본 연산 ==========

class TestBasicOperations:
    """기본 사칙연산 테스트"""

    def test_두_숫자_덧셈(self):
        """2 + 3 = 5"""
        result = calculate("2 + 3")
        assert result == 5

    def test_다른_숫자_덧셈(self):
        """삼각측량: 10 + 7 = 17"""
        result = calculate("10 + 7")
        assert result == 17

    def test_뺄셈(self):
        """10 - 4 = 6"""
        result = calculate("10 - 4")
        assert result == 6

    def test_큰_숫자_뺄셈(self):
        """100 - 37 = 63"""
        result = calculate("100 - 37")
        assert result == 63

    def test_곱셈(self):
        """6 * 7 = 42"""
        result = calculate("6 * 7")
        assert result == 42

    def test_나눗셈(self):
        """20 / 4 = 5.0"""
        result = calculate("20 / 4")
        assert result == 5.0

    def test_나눗셈_소수(self):
        """10 / 3 = 3.333..."""
        result = calculate("10 / 3")
        assert abs(result - 3.333333) < 0.0001

    def test_공백_처리(self):
        """공백이 있어도 작동: "  2  +  3  " = 5"""
        result = calculate("  2  +  3  ")
        assert result == 5


# ========== Phase 2: 복합 연산 ==========

class TestComplexOperations:
    """복합 연산 테스트"""

    def test_여러_덧셈(self):
        """2 + 3 + 4 = 9"""
        result = calculate("2 + 3 + 4")
        assert result == 9

    def test_여러_뺄셈(self):
        """20 - 5 - 3 = 12"""
        result = calculate("20 - 5 - 3")
        assert result == 12

    def test_덧셈_뺄셈_혼합(self):
        """10 + 5 - 3 = 12"""
        result = calculate("10 + 5 - 3")
        assert result == 12

    def test_여러_곱셈(self):
        """2 * 3 * 4 = 24"""
        result = calculate("2 * 3 * 4")
        assert result == 24

    def test_여러_나눗셈(self):
        """100 / 5 / 2 = 10.0"""
        result = calculate("100 / 5 / 2")
        assert result == 10.0

    def test_긴_수식(self):
        """1 + 2 + 3 + 4 + 5 = 15"""
        result = calculate("1 + 2 + 3 + 4 + 5")
        assert result == 15


# ========== Phase 3: 연산자 우선순위 ==========

class TestOperatorPriority:
    """연산자 우선순위 테스트"""

    def test_곱셈_우선순위(self):
        """2 + 3 * 4 = 14 (곱셈 먼저!)"""
        result = calculate("2 + 3 * 4")
        assert result == 14

    def test_나눗셈_우선순위(self):
        """10 - 20 / 4 = 5.0"""
        result = calculate("10 - 20 / 4")
        assert result == 5.0

    def test_복잡한_우선순위(self):
        """2 + 3 * 4 - 10 / 2 = 9.0"""
        result = calculate("2 + 3 * 4 - 10 / 2")
        assert result == 9.0

    def test_곱셈_나눗셈_혼합(self):
        """2 * 3 / 2 = 3.0"""
        result = calculate("2 * 3 / 2")
        assert result == 3.0

    def test_여러_우선순위_연산(self):
        """5 + 2 * 3 - 4 / 2 = 9.0"""
        result = calculate("5 + 2 * 3 - 4 / 2")
        assert result == 9.0


# ========== Phase 4: 괄호 처리 ==========

class TestParentheses:
    """괄호 처리 테스트"""

    def test_단일_괄호(self):
        """(2 + 3) * 4 = 20"""
        result = calculate("(2 + 3) * 4")
        assert result == 20

    def test_괄호_우선순위_변경(self):
        """10 - (2 * 3) = 4"""
        result = calculate("10 - (2 * 3)")
        assert result == 4

    def test_중첩_괄호(self):
        """((2 + 3) * 4) / 5 = 4.0"""
        result = calculate("((2 + 3) * 4) / 5")
        assert result == 4.0

    def test_여러_괄호(self):
        """(2 + 3) * (4 + 5) = 45"""
        result = calculate("(2 + 3) * (4 + 5)")
        assert result == 45

    def test_복잡한_괄호(self):
        """((2 + 3) * 4 - 10) / 2 = 5.0"""
        result = calculate("((2 + 3) * 4 - 10) / 2")
        assert result == 5.0

    def test_괄호_안_복잡한_수식(self):
        """(10 + 5 - 3) * 2 = 24"""
        result = calculate("(10 + 5 - 3) * 2")
        assert result == 24


# ========== Phase 5: Edge Cases ==========

class TestEdgeCases:
    """예외 상황 테스트"""

    def test_0으로_나누기(self):
        """0으로 나누면 ZeroDivisionError"""
        with pytest.raises(ZeroDivisionError, match="Division by zero"):
            calculate("10 / 0")

    def test_괄호_안에서_0으로_나누기(self):
        """괄호 안에서 0으로 나누기"""
        with pytest.raises(ZeroDivisionError):
            calculate("(10 / 0) + 5")

    def test_빈_문자열(self):
        """빈 문자열은 ValueError"""
        with pytest.raises(ValueError, match="cannot be empty"):
            calculate("")

    def test_공백만_있는_문자열(self):
        """공백만 있으면 ValueError"""
        with pytest.raises(ValueError):
            calculate("   ")

    def test_불완전한_수식_연산자로_끝남(self):
        """연산자로 끝나면 ValueError"""
        with pytest.raises(ValueError, match="ends with operator"):
            calculate("2 +")

    def test_불완전한_수식_연산자로_시작(self):
        """연산자로 시작하면 ValueError"""
        with pytest.raises(ValueError, match="Invalid token"):
            calculate("+ 3")

    def test_잘못된_문자(self):
        """숫자가 아닌 문자는 ValueError"""
        with pytest.raises(ValueError):
            calculate("abc")

    def test_연산자만(self):
        """연산자만 있으면 ValueError"""
        with pytest.raises(ValueError):
            calculate("+")

    def test_숫자만(self):
        """숫자만 있으면 정상 작동"""
        result = calculate("42")
        assert result == 42


# ========== 통합 시나리오 테스트 ==========

class TestIntegrationScenarios:
    """실제 사용 시나리오 테스트"""

    def test_복잡한_실전_수식_1(self):
        """(5 + 3) * 2 - 10 / 2 = 11.0"""
        result = calculate("(5 + 3) * 2 - 10 / 2")
        assert result == 11.0

    def test_복잡한_실전_수식_2(self):
        """100 - (20 + 30) * 2 + 50 / 5 = 10.0"""
        result = calculate("100 - (20 + 30) * 2 + 50 / 5")
        assert result == 10.0

    def test_복잡한_실전_수식_3(self):
        """((10 + 20) / 3) * 2 = 20.0"""
        result = calculate("((10 + 20) / 3) * 2")
        assert result == 20.0

    def test_매우_긴_수식(self):
        """1 + 2 * 3 - 4 / 2 + 5 = 10.0"""
        result = calculate("1 + 2 * 3 - 4 / 2 + 5")
        assert result == 10.0

    def test_모든_연산자_사용(self):
        """10 + 5 - 3 * 2 / 2 = 12.0"""
        result = calculate("10 + 5 - 3 * 2 / 2")
        assert result == 12.0


# ========== 성능 테스트 (선택) ==========

class TestPerformance:
    """성능 관련 테스트"""

    def test_매우_긴_수식_계산(self):
        """매우 긴 수식도 처리 가능"""
        # 1 + 1 + 1 + ... (100번)
        expression = " + ".join(["1"] * 100)
        result = calculate(expression)
        assert result == 100

    def test_깊은_중첩_괄호(self):
        """깊게 중첩된 괄호 처리"""
        result = calculate("((((2 + 3)))))")
        assert result == 5
