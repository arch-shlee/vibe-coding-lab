# 01 - Red-Green-Refactor 심화: TDD 마스터하기

> 복잡한 비즈니스 로직을 TDD로 구현하며 고급 TDD 기법을 익힙니다.

## 🎯 학습 목표

- TDD를 복잡한 비즈니스 로직에 적용하기
- Edge case와 예외 상황을 체계적으로 처리하기
- 리팩토링 타이밍을 적절히 판단하기
- 테스트 코드의 품질을 향상시키기
- Red-Green-Refactor 사이클을 자연스럽게 실천하기

**예상 소요 시간**: 4-5시간

---

## 📚 학습 내용

### Level 1 vs Level 2

**Level 1에서 배운 것**:
- Red-Green-Refactor의 기본 사이클
- 간단한 함수 테스트
- 기본적인 예외 처리

**Level 2에서 배울 것**:
- 복잡한 비즈니스 로직을 작은 단위로 나누기
- 다양한 Edge case 발견하고 처리하기
- 리팩토링의 타이밍과 범위 결정하기
- 테스트를 문서로 활용하기

### TDD 심화 개념

#### 1. 삼각측량 (Triangulation)

**문제**: 너무 빨리 일반화하면 잘못된 추상화가 될 수 있음

**해결**: 구체적인 예시 2-3개로 패턴을 확인

```python
# 첫 번째 테스트
def test_더하기_2_더하기_3():
    assert calculate("2 + 3") == 5

# 두 번째 테스트 (삼각측량)
def test_더하기_5_더하기_7():
    assert calculate("5 + 7") == 12

# 이제 패턴이 명확함 → 일반화된 구현
```

#### 2. 명백한 구현 (Obvious Implementation)

**언제**: 구현이 자명할 때

```python
# 테스트
def test_숫자_파싱():
    assert parse_number("42") == 42

# 구현 - 바로 정답 작성
def parse_number(s):
    return int(s)
```

#### 3. 가짜 구현 (Fake It)

**언제**: 구현이 복잡하고 불명확할 때

```python
# 테스트
def test_복잡한_계산():
    assert complex_calc(x, y) == expected

# 구현 - 일단 하드코딩
def complex_calc(x, y):
    return expected  # 가짜!

# 테스트 추가하면서 점진적으로 실제 구현으로 교체
```

#### 4. 리팩토링 신호

**언제 리팩토링할까?**:
- ✅ 모든 테스트가 초록불일 때
- ✅ 중복 코드가 보일 때
- ✅ 함수가 너무 길어질 때
- ✅ 이름이 명확하지 않을 때

**언제 리팩토링을 멈출까?**:
- ✅ 테스트가 빨간불로 바뀔 때 (롤백!)
- ✅ 새로운 기능을 추가하고 싶을 때 (일단 커밋)

---

## 🚀 실습: 고급 계산기 구현

### 프로젝트 개요

Level 1에서는 간단한 계산기를 만들었습니다.
Level 2에서는 **실제 계산기처럼** 문자열 수식을 계산하는 계산기를 TDD로 만듭니다.

### 요구사항

#### Phase 1: 기본 연산
```python
calculate("2 + 3")      # 5
calculate("10 - 4")     # 6
calculate("3 * 4")      # 12
calculate("20 / 5")     # 4.0
```

#### Phase 2: 복합 연산
```python
calculate("2 + 3 + 4")           # 9
calculate("10 - 3 + 2")          # 9
calculate("2 * 3 * 4")           # 24
```

#### Phase 3: 연산자 우선순위
```python
calculate("2 + 3 * 4")           # 14 (not 20!)
calculate("10 - 2 * 3")          # 4
calculate("20 / 4 + 3")          # 8.0
```

#### Phase 4: 괄호 처리
```python
calculate("(2 + 3) * 4")         # 20
calculate("10 - (2 * 3)")        # 4
calculate("((2 + 3) * 4) / 5")   # 4.0
```

#### Phase 5: Edge Cases
```python
calculate("10 / 0")              # ZeroDivisionError
calculate("2 +")                 # ValueError (불완전한 수식)
calculate("abc")                 # ValueError (잘못된 입력)
calculate("")                    # ValueError (빈 문자열)
calculate("  2  +  3  ")         # 5 (공백 처리)
```

---

## 💡 학습 전략

### TDD 사이클을 엄격히 지키기

**규칙**:
1. 테스트 없이는 구현 코드를 작성하지 않는다
2. 실패하는 테스트를 보기 전에는 다음 테스트를 작성하지 않는다
3. 테스트를 통과하는 최소한의 코드만 작성한다

**이점**:
- 불필요한 기능을 만들지 않음
- 항상 작동하는 코드 유지
- 리팩토링에 대한 자신감

### 작은 단계로 나누기

**나쁜 예**:
```
"계산기 전체를 한 번에 구현하자"
→ 복잡하고, 디버깅 어렵고, 테스트 어려움
```

**좋은 예**:
```
1. 단일 숫자 파싱
2. 두 숫자 더하기
3. 빼기, 곱하기, 나누기 추가
4. 여러 연산 처리
5. 우선순위 추가
6. 괄호 추가
```

### 리팩토링은 초록불에서만

```
🔴 Red → 🟢 Green → 🔵 Refactor → 🔴 Red → ...
                ↑
         여기서만 리팩토링!
```

---

## 📝 실습 과제

### 과제 1: 기본 사칙연산 (필수)

**목표**: 단일 연산 처리

```python
# 테스트 예시
def test_덧셈():
    assert calculate("2 + 3") == 5

def test_뺄셈():
    assert calculate("10 - 4") == 6
```

**힌트**:
- 문자열을 파싱하는 방법 생각하기
- `split()` 메서드 활용
- 연산자별로 분기 처리

### 과제 2: 복합 연산 (필수)

**목표**: 같은 우선순위 연산 여러 개

```python
def test_여러_덧셈():
    assert calculate("1 + 2 + 3 + 4") == 10
```

**힌트**:
- 왼쪽부터 순서대로 계산
- 반복문 또는 재귀 고려

### 과제 3: 연산자 우선순위 (필수)

**목표**: * / 가 + - 보다 먼저

```python
def test_우선순위():
    assert calculate("2 + 3 * 4") == 14
```

**힌트**:
- 곱셈/나눗셈을 먼저 찾아서 계산
- 결과를 원래 위치에 대체

### 과제 4: 괄호 처리 (도전)

**목표**: 괄호 안을 먼저 계산

```python
def test_괄호():
    assert calculate("(2 + 3) * 4") == 20
```

**힌트**:
- 재귀적으로 접근
- 가장 안쪽 괄호부터 계산
- 계산 결과로 괄호 부분 교체

### 과제 5: Edge Cases (필수)

**목표**: 예외 상황 처리

```python
def test_0으로_나누기():
    with pytest.raises(ZeroDivisionError):
        calculate("10 / 0")

def test_잘못된_수식():
    with pytest.raises(ValueError):
        calculate("2 +")
```

---

## 🎓 리팩토링 연습

### 리팩토링 체크리스트

테스트가 모두 통과하면 다음을 점검하세요:

#### 코드 중복 제거
```python
# Before (중복!)
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b

# After (딕셔너리 활용)
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
result = operations[op](a, b)
```

#### 함수 분리
```python
# Before (긴 함수)
def calculate(expression):
    # 30줄짜리 코드...

# After (작은 함수들)
def calculate(expression):
    tokens = tokenize(expression)
    tokens = handle_parentheses(tokens)
    tokens = handle_multiply_divide(tokens)
    result = handle_add_subtract(tokens)
    return result
```

#### 명확한 이름
```python
# Before
def proc(s):
    t = s.split()
    ...

# After
def tokenize(expression):
    tokens = expression.split()
    ...
```

---

## ✅ 체크포인트

### Checkpoint 1: 기본 연산 ✅
- [ ] 덧셈 테스트 통과
- [ ] 뺄셈 테스트 통과
- [ ] 곱셈 테스트 통과
- [ ] 나눗셈 테스트 통과
- [ ] 각 연산마다 Red-Green-Refactor 사이클을 따랐다

### Checkpoint 2: 복합 연산 ✅
- [ ] 여러 덧셈 테스트 통과
- [ ] 여러 연산 혼합 테스트 통과
- [ ] 코드에 중복이 없다

### Checkpoint 3: 우선순위 ✅
- [ ] 곱셈 우선순위 테스트 통과
- [ ] 나눗셈 우선순위 테스트 통과
- [ ] 함수가 적절히 분리되었다

### Checkpoint 4: 괄호 (선택) ✅
- [ ] 단일 괄호 테스트 통과
- [ ] 중첩 괄호 테스트 통과

### Checkpoint 5: Edge Cases ✅
- [ ] 0으로 나누기 예외 처리
- [ ] 잘못된 수식 예외 처리
- [ ] 빈 문자열 예외 처리
- [ ] 공백 처리

---

## 📚 학습 정리

### Red-Green-Refactor 실천 경험

**Red (빨강)**:
- 무엇을 배웠나요?
- 어떤 테스트를 먼저 작성하는 게 좋았나요?

**Green (초록)**:
- 최소한의 코드는 어느 정도였나요?
- 처음부터 완벽한 코드를 작성하지 않아도 괜찮았나요?

**Refactor (파랑)**:
- 언제 리팩토링했나요?
- 어떤 것을 개선했나요?
- 테스트가 안전망 역할을 했나요?

### 삼각측량의 가치

- 구체적인 예시가 추상화에 도움이 되었나요?
- 몇 개의 테스트가 적당했나요?

---

## 🔗 다음 단계

### 이 모듈을 완료했다면

1. [02-single-agent](../02-single-agent/README.md)로 진행
2. AI 에이전트를 최적으로 활용하는 방법 학습
3. Gemini vs Claude 비교 및 선택

### 추가 도전 과제

- [ ] 소수점 연산 지원
- [ ] 음수 처리
- [ ] 과학 계산 함수 (sin, cos, sqrt 등)
- [ ] 변수 지원 (x = 5, calculate("x + 3"))

---

## 🆘 막혔나요?

### 자주 하는 질문

**Q: 테스트를 먼저 작성하는 게 어려워요**
A: 가장 간단한 케이스부터 시작하세요. "2 + 3"처럼 구체적인 예시로!

**Q: 리팩토링을 언제 해야 할지 모르겠어요**
A: 중복이 보이거나, 함수가 10줄 이상이면 고려하세요.

**Q: 괄호 처리가 너무 어려워요**
A: 선택 과제입니다! 기본만 완성해도 충분합니다.

### 추가 도움
- [GUIDE.md](./GUIDE.md): 상세한 단계별 가이드
- [checkpoints/](./checkpoints/): 진행 상황 점검
- [solution/](./solution/): 막힐 때만 참고

---

**모듈**: 01-red-green-refactor
**레벨**: Level 2 (중급)
**난이도**: ⭐⭐⭐☆☆
**예상 시간**: 4-5시간
**작성일**: 2026-01-18
