# 02-first-tdd 단계별 실습 가이드

> 이 가이드를 따라하면서 TDD의 Red-Green-Refactor 사이클을 체험하세요.

## 🎯 이 가이드의 목표

- TDD 사이클을 직접 경험하기
- pytest로 테스트 작성 및 실행하기
- 간단한 계산기를 TDD로 완성하기

**소요 시간**: 3-4시간

---

## 📋 사전 준비

### 1. 환경 확인

```bash
# Python 버전 확인
python --version  # 3.9 이상

# pytest 설치 확인
pytest --version

# 설치 안 되어 있다면
pip install pytest
```

### 2. 작업 폴더로 이동

```bash
cd level-1-basics/02-first-tdd/starter
```

### 3. 파일 구조 확인

```
starter/
├── calculator.py         # 여기에 함수를 작성할 예정
└── test_calculator.py    # 여기에 테스트를 작성할 예정
```

---

## 🔴 Part 1: 첫 번째 Red-Green-Refactor (덧셈)

### Step 1-1: 🔴 Red - 실패하는 테스트 작성

`test_calculator.py`를 열고 첫 번째 테스트를 작성하세요:

```python
# test_calculator.py
from calculator import add

def test_add_two_positive_numbers():
    """두 양수를 더하는 테스트"""
    result = add(2, 3)
    assert result == 5
```

**AI에게 요청** (선택사항):
```
pytest로 add 함수를 테스트하는 코드를 작성해줘.
2와 3을 더하면 5가 나오는지 검증하는 테스트야.
```

### Step 1-2: 테스트 실행 (실패 확인)

```bash
pytest test_calculator.py -v
```

**예상 결과**: 🔴 실패
```
ImportError: cannot import name 'add' from 'calculator'
```

✅ **축하합니다!** 첫 번째 Red 단계 완료. 실패가 정상입니다!

### Step 1-3: 🟢 Green - 최소 코드 작성

`calculator.py`를 열고 테스트를 통과할 최소 코드만 작성하세요:

```python
# calculator.py
def add(a, b):
    return a + b
```

**AI에게 요청** (선택사항):
```
test_add_two_positive_numbers 테스트를 통과하는
가장 간단한 add 함수를 작성해줘.
```

### Step 1-4: 테스트 실행 (통과 확인)

```bash
pytest test_calculator.py -v
```

**예상 결과**: 🟢 통과
```
test_calculator.py::test_add_two_positive_numbers PASSED
```

✅ **축하합니다!** 첫 번째 Green 단계 완료!

### Step 1-5: 🔵 Refactor - 코드 개선

테스트가 통과했으니 코드를 개선할 수 있습니다:

```python
# calculator.py
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
    """
    return a + b
```

### Step 1-6: 테스트 다시 실행

```bash
pytest test_calculator.py -v
```

**예상 결과**: 🟢 여전히 통과

✅ **축하합니다!** 첫 번째 Red-Green-Refactor 사이클 완료! 🎉

---

## 🔴 Part 2: 두 번째 사이클 (뺄셈)

이제 혼자서 해보세요!

### Step 2-1: 🔴 Red - 뺄셈 테스트

`test_calculator.py`에 추가:

```python
def test_subtract_two_numbers():
    """두 숫자를 빼는 테스트"""
    result = subtract(5, 3)
    assert result == 2
```

**실행**: `pytest test_calculator.py -v` → 🔴 실패 확인

### Step 2-2: 🟢 Green - subtract 함수 작성

`calculator.py`에 추가:

```python
def subtract(a, b):
    return a - b
```

**실행**: `pytest test_calculator.py -v` → 🟢 통과 확인

### Step 2-3: 🔵 Refactor - 개선

타입 힌트와 docstring 추가:

```python
def subtract(a: float, b: float) -> float:
    """두 숫자를 뺍니다."""
    return a - b
```

**실행**: `pytest test_calculator.py -v` → 🟢 여전히 통과

---

## 🔴 Part 3: 세 번째 사이클 (곱셈)

### Step 3-1: 테스트 작성

```python
def test_multiply_two_numbers():
    """두 숫자를 곱하는 테스트"""
    result = multiply(4, 3)
    assert result == 12
```

### Step 3-2: 함수 작성

```python
def multiply(a: float, b: float) -> float:
    """두 숫자를 곱합니다."""
    return a * b
```

### Step 3-3: 확인

```bash
pytest test_calculator.py -v
```

---

## 🔴 Part 4: 네 번째 사이클 (나눗셈)

### Step 4-1: 기본 테스트

```python
def test_divide_two_numbers():
    """두 숫자를 나누는 테스트"""
    result = divide(10, 2)
    assert result == 5
```

### Step 4-2: 함수 작성

```python
def divide(a: float, b: float) -> float:
    """두 숫자를 나눕니다."""
    return a / b
```

### Step 4-3: Edge Case - 0으로 나누기

**새로운 테스트 추가**:

```python
import pytest

def test_divide_by_zero():
    """0으로 나누면 예외 발생"""
    with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
        divide(10, 0)
```

**실행**: 🔴 실패 (ZeroDivisionError 발생)

**함수 수정**:

```python
def divide(a: float, b: float) -> float:
    """
    두 숫자를 나눕니다.

    Raises:
        ValueError: b가 0일 때
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b
```

**실행**: 🟢 통과!

---

## 🎯 Part 5: 추가 테스트 케이스

### 음수 테스트

```python
def test_add_negative_numbers():
    """음수 덧셈 테스트"""
    assert add(-5, -3) == -8
    assert add(-5, 3) == -2

def test_subtract_negative_numbers():
    """음수 뺄셈 테스트"""
    assert subtract(-5, -3) == -2
    assert subtract(5, -3) == 8
```

### 소수점 테스트

```python
def test_add_floats():
    """소수점 덧셈 테스트"""
    result = add(0.1, 0.2)
    assert abs(result - 0.3) < 0.0001  # 부동소수점 오차 고려
```

---

## 🚀 Part 6: AI와 함께 TDD

### AI 활용 전략

**단계 1: 테스트 요청**

```
"문자열을 뒤집는 reverse_string 함수를 테스트하는
pytest 코드를 작성해줘. 'hello'를 입력하면 'olleh'가
나와야 해."
```

**단계 2: 테스트 실행 및 실패 확인**

```bash
pytest test_string_utils.py -v
# 🔴 실패 확인
```

**단계 3: 구현 요청**

```
"위 테스트를 통과하는 reverse_string 함수를
작성해줘. 가장 간단한 방법으로."
```

**단계 4: 리팩토링 요청**

```
"reverse_string 함수에 타입 힌트와 docstring을
추가해줘. 더 명확하게 만들어줘."
```

### AI 대화 예시

**You**:
```
문자열의 모음(a,e,i,o,u) 개수를 세는 count_vowels 함수를
테스트하는 pytest 코드를 작성해줘.
"hello"는 2개의 모음이 있어.
```

**AI**:
```python
def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0
```

**You**: 테스트 실행 → 🔴 실패 확인 → 다시 요청

```
이 테스트를 통과하는 count_vowels 함수를 작성해줘.
```

---

## ✅ 최종 확인

### 모든 테스트 실행

```bash
# 모든 테스트 실행
pytest test_calculator.py -v

# 커버리지 확인 (선택사항)
pytest test_calculator.py --cov=calculator
```

### 예상 출력

```
test_calculator.py::test_add_two_positive_numbers PASSED
test_calculator.py::test_subtract_two_numbers PASSED
test_calculator.py::test_multiply_two_numbers PASSED
test_calculator.py::test_divide_two_numbers PASSED
test_calculator.py::test_divide_by_zero PASSED
test_calculator.py::test_add_negative_numbers PASSED
test_calculator.py::test_subtract_negative_numbers PASSED

==================== 7 passed in 0.03s ====================
```

---

## 🎓 학습 정리

### 완료한 것들

- [x] TDD 사이클 4번 반복 (add, subtract, multiply, divide)
- [x] pytest 테스트 작성 및 실행
- [x] Red-Green-Refactor 경험
- [x] Edge case 처리 (0으로 나누기)
- [x] AI와 협업하며 TDD 실습

### 핵심 교훈

1. **테스트가 먼저**: 코드 작성 전에 테스트 작성
2. **작은 단계**: 한 번에 하나씩
3. **빨간불을 두려워하지 말것**: 실패는 과정의 일부
4. **리팩토링의 자신감**: 테스트가 안전망
5. **AI는 조수**: 방향은 내가 결정

---

## 🔗 다음 단계

1. [checkpoints/](./checkpoints/) 폴더에서 진행 상황 확인
2. [solution/](./solution/) 폴더의 완성 코드와 비교
3. [03-ai-assistant](../03-ai-assistant/) 모듈로 이동

---

## 💡 추가 도전 과제

### 도전 1: 문자열 유틸리티

TDD로 다음 함수들을 구현하세요:

1. `reverse_string(s)`: 문자열 뒤집기
2. `count_vowels(s)`: 모음 개수
3. `is_palindrome(s)`: 회문 판별

### 도전 2: 리스트 유틸리티

1. `find_max(numbers)`: 최댓값 찾기
2. `find_min(numbers)`: 최솟값 찾기
3. `calculate_average(numbers)`: 평균 계산

### 도전 3: 에러 처리

각 함수에 적절한 예외 처리 추가:
- 빈 리스트 처리
- None 값 처리
- 잘못된 타입 처리

---

**작성일**: 2026-01-13
**난이도**: ⭐⭐☆☆☆
**예상 완료 시간**: 3-4시간
