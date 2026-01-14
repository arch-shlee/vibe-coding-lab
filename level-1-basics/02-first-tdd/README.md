# 02 - First TDD: TDD 입문

> Red-Green-Refactor 사이클을 체험하며 테스트 주도 개발의 기초를 배웁니다.

## 🎯 학습 목표

- TDD(Test-Driven Development)가 무엇인지 이해하기
- Red-Green-Refactor 사이클 직접 체험하기
- pytest로 테스트 작성 및 실행하기
- 테스트 먼저, 구현은 나중에 하는 습관 익히기
- AI와 함께 TDD 실습하기

**예상 소요 시간**: 3-4시간

---

## 📚 TDD란?

### Test-Driven Development (테스트 주도 개발)

**TDD**는 코드를 작성하기 **전에** 테스트를 먼저 작성하는 개발 방법론입니다.

**전통적 개발**:
```
코드 작성 → 실행 → 버그 발견 → 수정 → 반복
```

**TDD**:
```
테스트 작성 → 코드 작성 → 테스트 실행 → 리팩토링 → 반복
```

### TDD의 장점

✅ **버그 조기 발견**
- 테스트가 코드 품질을 보장

✅ **자신감 있는 리팩토링**
- 테스트가 있으면 코드 수정이 두렵지 않음

✅ **명확한 요구사항**
- 테스트가 곧 요구사항 문서

✅ **설계 개선**
- 테스트하기 쉬운 코드는 좋은 설계

---

## 🔄 Red-Green-Refactor 사이클

TDD의 핵심은 3단계 사이클입니다:

### 🔴 Red (빨강): 실패하는 테스트 작성

1. **무엇을 만들지 결정**
2. **그것을 검증하는 테스트 작성**
3. **테스트 실행** → 당연히 실패 (코드가 없으니까!)
4. 실패 메시지 확인 (빨간불 🔴)

```python
# 예: test_calculator.py
def test_add():
    result = add(2, 3)
    assert result == 5  # 실패! add 함수가 없음
```

### 🟢 Green (초록): 테스트 통과하는 최소 코드

1. **테스트를 통과할 최소한의 코드만 작성**
2. "일단 되게 만들고, 나중에 좋게 만들자"
3. **테스트 실행** → 성공 (초록불 🟢)

```python
# 예: calculator.py
def add(a, b):
    return a + b  # 가장 간단한 구현
```

### 🔵 Refactor (파랑): 코드 개선

1. **작동하는 코드를 더 좋게 개선**
2. 중복 제거, 이름 개선, 구조 정리
3. **테스트 실행** → 여전히 통과 확인
4. 테스트는 안전망 역할

```python
# 예: calculator.py (리팩토링 후)
def add(a: float, b: float) -> float:
    """
    두 숫자를 더합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        두 숫자의 합
    """
    return a + b
```

### 사이클 반복

```
🔴 Red → 🟢 Green → 🔵 Refactor → 🔴 Red → 🟢 Green → ...
```

---

## 🛠️ pytest 기본 사용법

### pytest란?

Python의 테스트 프레임워크. 간단하고 강력합니다.

### 기본 문법

```python
# test_example.py
def test_something():
    # Given (준비)
    x = 10

    # When (실행)
    result = x + 5

    # Then (검증)
    assert result == 15
```

### 실행 방법

```bash
# 모든 테스트 실행
pytest

# 특정 파일만
pytest test_calculator.py

# 상세 출력
pytest -v

# 실패 시 자세한 정보
pytest -vv
```

### assert 문법

```python
assert value == expected          # 같은지
assert value != expected          # 다른지
assert value > 10                 # 크기 비교
assert value in [1, 2, 3]        # 포함 여부
assert isinstance(value, int)     # 타입 확인
```

---

## 💡 실습: 간단한 계산기

### 목표

TDD로 간단한 계산기를 만들어봅니다:
- 덧셈 (add)
- 뺄셈 (subtract)
- 곱셈 (multiply)
- 나눗셈 (divide)

### 실습 순서

#### 1. Red: 덧셈 테스트 작성

```python
# test_calculator.py
def test_add():
    result = add(2, 3)
    assert result == 5
```

실행: `pytest test_calculator.py` → 🔴 실패

#### 2. Green: 최소 구현

```python
# calculator.py
def add(a, b):
    return a + b
```

실행: `pytest test_calculator.py` → 🟢 통과!

#### 3. Refactor: 코드 개선

타입 힌트, docstring 추가

#### 4. 반복: 뺄셈, 곱셈, 나눗셈

같은 사이클로 나머지 함수들도 구현

---

## 📝 과제

### 과제 1: 계산기 기본 연산 (TDD)

`starter/` 폴더에서 시작하세요.

**요구사항**:
1. `add(a, b)`: 덧셈
2. `subtract(a, b)`: 뺄셈
3. `multiply(a, b)`: 곱셈
4. `divide(a, b)`: 나눗셈

**TDD 순서**:
1. 각 함수마다 테스트 먼저 작성
2. 테스트 실행 (🔴 실패 확인)
3. 최소 코드 작성
4. 테스트 실행 (🟢 통과 확인)
5. 리팩토링
6. 다음 함수로 이동

**AI 활용 팁**:
```
"pytest로 add 함수를 테스트하는 코드를 작성해줘.
2 + 3 = 5를 검증하는 테스트야."
```

### 과제 2: Edge Case 처리

**추가 요구사항**:
- 0으로 나누기 처리
- 음수 처리
- 소수점 처리

**테스트 예시**:
```python
def test_divide_by_zero():
    # 0으로 나누면 예외 발생해야 함
    with pytest.raises(ValueError):
        divide(10, 0)
```

### 과제 3: 문자열 처리 함수 (도전!)

TDD로 다음 함수들을 구현하세요:

1. `reverse_string(s)`: 문자열 뒤집기
2. `count_vowels(s)`: 모음 개수 세기
3. `is_palindrome(s)`: 회문 판별

---

## ✅ 체크포인트

### Checkpoint 1: TDD 이해

- [ ] TDD가 무엇인지 설명할 수 있다
- [ ] Red-Green-Refactor 사이클을 이해한다
- [ ] 왜 테스트를 먼저 작성하는지 안다

### Checkpoint 2: pytest 사용

- [ ] pytest 설치 및 실행 가능
- [ ] 간단한 테스트 작성 가능
- [ ] assert 문 사용 가능
- [ ] 테스트 실행 결과 읽을 수 있음

### Checkpoint 3: TDD 실습

- [ ] 계산기 4개 함수 TDD로 완성
- [ ] 각 함수마다 테스트 먼저 작성
- [ ] Red-Green-Refactor 사이클 경험
- [ ] 모든 테스트 통과

### Checkpoint 4: Edge Case

- [ ] 0으로 나누기 예외 처리
- [ ] 예외 테스트 작성 가능
- [ ] 다양한 입력값 테스트

---

## 🎓 학습 정리

### TDD의 핵심 규칙

**규칙 1: 실패하는 테스트를 먼저 작성**
- 코드보다 테스트가 먼저

**규칙 2: 최소한의 코드만 작성**
- 테스트 통과가 목표
- 과도한 설계 금지

**규칙 3: 리팩토링으로 개선**
- 테스트가 안전망
- 자신있게 코드 개선

### AI와 TDD

**좋은 예시**:
```
"add 함수를 테스트하는 pytest 코드를 작성해줘.
그리고 그 테스트를 통과하는 최소한의 add 함수도 작성해줘."
```

**더 좋은 예시**:
```
"먼저 add 함수를 테스트하는 코드만 작성해줘.
(테스트가 실패하는 걸 확인한 후)
이제 이 테스트를 통과하는 add 함수를 작성해줘."
```

---

## 🆘 막혔나요?

### 자주 하는 질문

**Q: 테스트를 어떻게 작성하나요?**
A: `test_`로 시작하는 함수를 만들고, `assert`로 검증하세요.

**Q: pytest를 찾을 수 없어요**
A: 가상환경이 활성화되었는지 확인하고 `pip install pytest`

**Q: 테스트가 실패해요**
A: 🔴 Red 단계에서는 실패가 정상입니다! 이제 코드를 작성하세요.

**Q: 리팩토링을 언제 하나요?**
A: 테스트가 통과한 후(🟢 Green). 테스트가 안전망 역할을 합니다.

### 추가 도움

- [GUIDE.md](./GUIDE.md): 단계별 상세 가이드
- [solution/](./solution/): 모범 답안
- [checkpoints/](./checkpoints/): 진행 상황 체크

---

## 🔗 다음 단계

02-first-tdd를 완료했다면:

1. [03-ai-assistant](../03-ai-assistant/README.md)로 이동
2. AI를 더 효과적으로 활용하는 방법 학습
3. 프롬프트 엔지니어링 실습

---

## 💬 학습 후기

이 모듈이 도움이 되었나요?

- TDD를 처음 경험한 소감은?
- 가장 어려웠던 부분은?
- [GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)에 공유해주세요

---

**모듈**: 02-first-tdd
**레벨**: Level 1 (기초)
**난이도**: ⭐⭐☆☆☆
**예상 시간**: 3-4시간
**작성일**: 2026-01-13
