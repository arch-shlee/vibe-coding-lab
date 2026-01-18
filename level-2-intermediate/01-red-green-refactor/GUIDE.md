# Red-Green-Refactor 심화 가이드

> 고급 계산기를 TDD로 구현하며 TDD 마스터가 되는 완전한 가이드입니다.

## 📖 이 가이드 사용법

### 학습 철학

이 가이드는 **생각하는 과정**을 보여줍니다.

- ✅ "왜 이 테스트를 먼저 작성하나요?"
- ✅ "왜 이렇게 구현하나요?"
- ✅ "언제 리팩토링하나요?"
- ✅ "다음 단계는 무엇인가요?"

### 추천 학습 방법

1. **한 Phase씩**: 한 번에 한 단계만 집중
2. **직접 타이핑**: 복사-붙여넣기 금지!
3. **AI와 대화**: 가이드는 참고만, 실제는 AI와 함께
4. **자주 커밋**: 각 단계마다 git commit

---

## 🎯 전체 로드맵

### Phase 1: 단일 연산 (1-1.5시간)
- 문자열 파싱
- 기본 사칙연산 (+, -, *, /)
- 첫 리팩토링 경험

### Phase 2: 복합 연산 (1시간)
- 여러 연산 처리
- 반복 패턴 발견
- 코드 중복 제거

### Phase 3: 연산자 우선순위 (1-1.5시간)
- * / 우선 처리
- 알고리즘 설계
- 함수 분리

### Phase 4: 괄호 처리 (선택, 1-2시간)
- 재귀적 접근
- 고급 알고리즘

### Phase 5: Edge Cases (30분)
- 예외 처리
- 입력 검증
- 최종 안정화

---

## Phase 1: 단일 연산 구현

### 목표
"2 + 3" 같은 단일 연산을 계산하는 계산기

### Step 1.1: 프로젝트 설정

```bash
# starter 폴더로 이동
cd level-2-intermediate/01-red-green-refactor/starter

# 가상 환경 (선택)
python -m venv venv
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

**확인**:
```bash
pytest --version  # pytest가 설치되었는지 확인
```

### Step 1.2: 첫 번째 테스트 - 덧셈

**🤔 사고 과정**:
- 가장 간단한 케이스는? → "2 + 3"
- 어떻게 사용될까? → `calculate("2 + 3")` → `5`
- 테스트로 표현하면?

**🔴 Red: 테스트 작성**

`test_calculator.py`에 추가:

```python
def test_두_숫자_덧셈():
    """가장 간단한 케이스: 2 + 3"""
    result = calculate("2 + 3")
    assert result == 5
```

**실행**:
```bash
pytest test_calculator.py -v
```

**예상 결과**: 🔴 `NameError: name 'calculate' is not defined`

**🟢 Green: 최소 구현**

**AI에게 요청**:
```
test_calculator.py에서 calculate 함수를 사용하고 있어.

calculator.py에 calculate 함수를 만들어줘.
지금은 "2 + 3"만 처리하면 돼.

가장 간단하게 구현해줘.
```

**예상 구현** (`calculator.py`):
```python
def calculate(expression):
    """
    간단한 수식을 계산합니다.

    Args:
        expression: 계산할 수식 문자열

    Returns:
        계산 결과
    """
    # 일단 하드코딩 (가짜 구현!)
    return 5
```

**테스트 실행**: 🟢 통과!

**🔵 Refactor: 개선**

**문제**: 하드코딩이라 "2 + 3"만 작동

**해결**: 실제로 파싱하기

**AI에게 요청**:
```
calculate 함수를 실제로 구현해줘.

문자열을 파싱해서:
1. 첫 번째 숫자 추출
2. 연산자 추출
3. 두 번째 숫자 추출
4. 연산 수행

split() 메서드를 사용해줘.
```

**리팩토링 후 테스트**: 🟢 여전히 통과!

### Step 1.3: 삼각측량 - 다른 덧셈

**🤔 사고 과정**:
- 정말 제대로 작동하나?
- 다른 숫자로 테스트해보자 (삼각측량!)

**🔴 Red: 테스트 추가**

```python
def test_다른_숫자_덧셈():
    """삼각측량: 다른 숫자로도 작동하는지 확인"""
    result = calculate("10 + 7")
    assert result == 17
```

**실행**: 🟢 통과! (이미 일반화된 구현이라서)

### Step 1.4: 뺄셈 추가

**🔴 Red**:
```python
def test_뺄셈():
    result = calculate("10 - 3")
    assert result == 7
```

**🟢 Green**:

**AI에게 요청**:
```
calculate 함수에 뺄셈도 지원하도록 수정해줘.
연산자가 '-'일 때 뺄셈을 수행하면 돼.
```

**🔵 Refactor**: 테스트 통과 확인 후 코드 정리

### Step 1.5: 곱셈, 나눗셈 추가

**같은 패턴 반복**:
1. 🔴 테스트 작성
2. 🟢 구현
3. 🔵 리팩토링

```python
def test_곱셈():
    result = calculate("6 * 7")
    assert result == 42

def test_나눗셈():
    result = calculate("20 / 4")
    assert result == 5.0
```

### Step 1.6: 리팩토링 - 중복 제거

**🤔 관찰**:
- `if op == '+'`, `elif op == '-'` ... 패턴 반복
- 중복 코드!

**🔵 Refactor**:

**AI에게 요청**:
```
calculator.py에 연산자 처리 로직이 반복돼.

딕셔너리를 사용해서 리팩토링해줘:
operations = {
    '+': lambda a, b: a + b,
    ...
}

이렇게 중복을 제거해줘.
```

**리팩토링 후**: 🟢 모든 테스트 통과 확인!

### Step 1.7: Phase 1 완료 체크

- [ ] 4가지 연산 (+, -, *, /) 모두 테스트 통과
- [ ] 코드에 중복이 없음
- [ ] 함수가 명확하고 읽기 쉬움
- [ ] 모든 테스트가 🟢 초록불

**커밋**:
```bash
git add .
git commit -m "feat: 단일 연산 계산기 완성 (Phase 1)"
```

---

## Phase 2: 복합 연산 구현

### 목표
"2 + 3 + 4" 같은 여러 연산 처리

### Step 2.1: 여러 덧셈

**🤔 사고 과정**:
- 이제 연산이 여러 개
- 왼쪽부터 순서대로 계산해야 함
- 어떻게 테스트할까?

**🔴 Red**:
```python
def test_여러_덧셈():
    """2 + 3 + 4 = 9"""
    result = calculate("2 + 3 + 4")
    assert result == 9
```

**실행**: 🔴 실패! (현재 구현은 2개만 처리)

**🟢 Green**:

**AI에게 요청**:
```
calculate 함수를 수정해서 여러 연산을 처리하도록 만들어줘.

예: "2 + 3 + 4" → 9

전략:
1. split()으로 모든 토큰 추출
2. 왼쪽부터 순서대로 계산
3. 반복문 사용

단계적으로 구현해줘.
```

**🔵 Refactor**: 코드 정리

### Step 2.2: 혼합 연산 (같은 우선순위)

**🔴 Red**:
```python
def test_덧셈_뺄셈_혼합():
    """10 + 5 - 3 = 12"""
    result = calculate("10 + 5 - 3")
    assert result == 12
```

**🟢 Green**: 이미 작동할 수도!

### Step 2.3: Phase 2 완료

**커밋**:
```bash
git commit -m "feat: 복합 연산 지원 (Phase 2)"
```

---

## Phase 3: 연산자 우선순위

### 목표
"2 + 3 * 4" = 14 (not 20!)

### Step 3.1: 문제 인식

**🔴 Red**:
```python
def test_곱셈_우선순위():
    """2 + 3 * 4 = 14 (곱셈 먼저!)"""
    result = calculate("2 + 3 * 4")
    assert result == 14
```

**실행**: 🔴 실패! (왼쪽부터 계산해서 20이 나옴)

### Step 3.2: 알고리즘 설계

**🤔 생각하기**:

**옵션 1: 우선순위 테이블**
- +, -: 우선순위 1
- *, /: 우선순위 2

**옵션 2: 두 단계로 나누기**
1. 곱셈/나눗셈 먼저 처리
2. 그 다음 덧셈/뺄셈 처리

**AI와 상의**:
```
"2 + 3 * 4"를 계산하려면 곱셈을 먼저 해야 해.

두 가지 방법을 생각했어:
1. 우선순위 테이블 사용
2. 두 단계로 나누기 (곱셈/나눗셈 → 덧셈/뺄셈)

어떤 방법이 더 단순하고 테스트하기 쉬울까?
구현 방법을 제안해줘.
```

### Step 3.3: 구현

**🟢 Green**:

**AI에게 요청**:
```
calculator.py를 수정해서 연산자 우선순위를 지원하도록 해줘.

알고리즘:
1. 토큰 리스트 생성
2. 먼저 *, / 찾아서 계산 → 결과로 교체
3. 그 다음 +, - 계산

단계적으로 구현해줘.
```

### Step 3.4: 함수 분리 (리팩토링)

**🔵 Refactor**:

**문제**: calculate 함수가 너무 길어짐

**해결**: 기능별로 분리

**AI에게 요청**:
```
calculate 함수가 너무 길어졌어.

다음 함수들로 분리해줘:
- tokenize(expression): 문자열을 토큰 리스트로
- apply_high_priority(tokens): *, / 처리
- apply_low_priority(tokens): +, - 처리
- calculate(expression): 위 함수들을 조합

각 함수에 docstring도 추가해줘.
```

**리팩토링 후**: 🟢 모든 테스트 통과!

### Step 3.5: 추가 테스트

```python
def test_나눗셈_우선순위():
    """10 - 20 / 4 = 5.0"""
    result = calculate("10 - 20 / 4")
    assert result == 5.0

def test_복잡한_우선순위():
    """2 + 3 * 4 - 10 / 2 = 9"""
    result = calculate("2 + 3 * 4 - 10 / 2")
    assert result == 9.0
```

### Step 3.6: Phase 3 완료

**커밋**:
```bash
git commit -m "feat: 연산자 우선순위 지원 (Phase 3)"
```

---

## Phase 4: 괄호 처리 (선택 과제)

### 목표
"(2 + 3) * 4" = 20

### Step 4.1: 괄호의 의미

**🤔 생각하기**:
- 괄호 안을 먼저 계산
- 결과로 괄호 부분 교체
- 재귀적으로 반복

### Step 4.2: 단일 괄호

**🔴 Red**:
```python
def test_단일_괄호():
    result = calculate("(2 + 3) * 4")
    assert result == 20
```

**🟢 Green**:

**AI에게 요청**:
```
괄호 처리를 추가하려고 해.

전략:
1. 가장 안쪽 괄호 찾기
2. 괄호 안 수식 계산
3. 결과로 괄호 부분 교체
4. 괄호가 없을 때까지 반복

재귀 또는 반복문으로 구현해줘.
```

### Step 4.3: 중첩 괄호

**🔴 Red**:
```python
def test_중첩_괄호():
    result = calculate("((2 + 3) * 4) / 2")
    assert result == 10.0
```

**🟢 Green**: 재귀 구현이면 이미 작동!

---

## Phase 5: Edge Cases

### 목표
예외 상황을 우아하게 처리

### Step 5.1: 0으로 나누기

**🔴 Red**:
```python
def test_0으로_나누기():
    with pytest.raises(ZeroDivisionError):
        calculate("10 / 0")
```

**🟢 Green**:

Python은 자동으로 `ZeroDivisionError`를 발생시킵니다!
별도 처리 필요 없음.

### Step 5.2: 잘못된 수식

**🔴 Red**:
```python
def test_불완전한_수식():
    with pytest.raises(ValueError, match="Invalid expression"):
        calculate("2 +")

def test_잘못된_문자():
    with pytest.raises(ValueError):
        calculate("abc")
```

**🟢 Green**:

**AI에게 요청**:
```
입력 검증을 추가해줘.

체크할 것:
- 빈 문자열
- 불완전한 수식 (연산자로 끝남)
- 잘못된 문자

ValueError를 발생시키고 명확한 메시지 포함해줘.
```

### Step 5.3: 공백 처리

**🔴 Red**:
```python
def test_공백_처리():
    result = calculate("  2  +  3  ")
    assert result == 5
```

**🟢 Green**:

`strip()`과 `split()`이 이미 처리!

---

## 🎯 최종 리팩토링

### 전체 코드 리뷰

**AI에게 요청**:
```
calculator.py 전체를 리뷰해줘.

체크 포인트:
- 함수 이름이 명확한가?
- 주석이 필요한 부분은?
- 중복 코드는 없는가?
- 타입 힌트가 있는가?
- docstring이 완전한가?

개선 제안을 해줘.
```

### 테스트 코드 정리

**구조화**:
```python
# test_calculator.py

class TestBasicOperations:
    """기본 사칙연산 테스트"""

    def test_덧셈(self):
        ...

    def test_뺄셈(self):
        ...

class TestComplexOperations:
    """복합 연산 테스트"""
    ...

class TestPriority:
    """우선순위 테스트"""
    ...

class TestEdgeCases:
    """예외 상황 테스트"""
    ...
```

---

## 💡 학습 팁

### TDD 사이클 체크리스트

매 테스트마다:
- [ ] 🔴 Red: 실패하는 테스트를 먼저 작성했다
- [ ] 🔴 Red: 테스트가 실패하는 것을 확인했다
- [ ] 🟢 Green: 최소한의 코드로 통과시켰다
- [ ] 🟢 Green: 테스트가 통과하는 것을 확인했다
- [ ] 🔵 Refactor: 중복을 제거하고 코드를 개선했다
- [ ] 🔵 Refactor: 리팩토링 후에도 테스트가 통과했다

### 막혔을 때

1. **더 작게 나누기**
   - 한 번에 하나의 기능만
   - 가장 간단한 케이스부터

2. **AI에게 물어보기**
   - 구체적인 상황 설명
   - 시도한 방법 공유
   - 에러 메시지 포함

3. **Solution 참고** (최후의 수단)
   - 전체가 아닌 힌트만
   - 이해하고 직접 작성

---

## 🎓 완료 후 활동

### 1. 회고록 작성

다음 질문에 답해보세요:

- TDD의 어떤 점이 좋았나요?
- 어떤 부분이 어려웠나요?
- 리팩토링을 언제 했나요?
- 다음에는 어떻게 하겠나요?

### 2. 추가 도전

- [ ] 소수점 숫자 지원
- [ ] 음수 처리
- [ ] 거듭제곱 연산자 (^)
- [ ] 과학 함수 (sqrt, sin, cos)

### 3. 다음 모듈

[02-single-agent](../02-single-agent/GUIDE.md)로 진행!

---

**작성일**: 2026-01-18
**버전**: 1.0
**예상 완료 시간**: 4-5시간
