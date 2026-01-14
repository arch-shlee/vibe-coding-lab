# 02-first-tdd: 모범 답안

> TDD로 작성된 완성된 계산기입니다.

## 📂 파일 구조

```
solution/
├── README.md            # 이 파일
├── calculator.py        # 완성된 계산기 함수들
├── test_calculator.py   # 완전한 테스트 스위트
└── string_utils.py      # 도전 과제 해답
```

## 🧪 테스트 실행

### 모든 테스트 실행

```bash
pytest test_calculator.py -v
```

**예상 결과**:
```
test_calculator.py::test_add_two_positive_numbers PASSED
test_calculator.py::test_add_negative_numbers PASSED
test_calculator.py::test_add_floats PASSED
...
==================== 25 passed in 0.05s ====================
```

### 커버리지 확인

```bash
pytest test_calculator.py --cov=calculator --cov-report=html
```

브라우저에서 `htmlcov/index.html`을 열어 커버리지 확인

## 📚 구현된 함수들

### 기본 연산

| 함수 | 설명 | 테스트 개수 |
|------|------|------------|
| `add(a, b)` | 덧셈 | 4개 |
| `subtract(a, b)` | 뺄셈 | 4개 |
| `multiply(a, b)` | 곱셈 | 4개 |
| `divide(a, b)` | 나눗셈 | 4개 |

### 추가 함수

| 함수 | 설명 | 특이사항 |
|------|------|---------|
| `power(base, exp)` | 거듭제곱 | 음수 지수 지원 |
| `modulo(a, b)` | 나머지 연산 | 0으로 나누기 예외 |

## 💡 TDD 특징

### 1. 테스트 우선 작성

모든 함수는 테스트가 먼저 작성되었습니다:
```python
# 1. 테스트 작성 (Red)
def test_add_two_positive_numbers():
    result = add(2, 3)
    assert result == 5

# 2. 구현 (Green)
def add(a, b):
    return a + b

# 3. 리팩토링 (Refactor)
def add(a: float, b: float) -> float:
    """두 숫자를 더합니다."""
    return a + b
```

### 2. Edge Case 커버

각 함수는 다양한 경우를 테스트합니다:
- ✅ 양수, 음수, 0
- ✅ 정수, 소수
- ✅ 큰 수, 작은 수
- ✅ 예외 상황 (0으로 나누기)

### 3. 명확한 문서화

모든 함수에 docstring 포함:
- 함수 설명
- 매개변수 설명
- 반환값 설명
- 발생 가능한 예외
- 사용 예시

## 🔍 코드 품질

### 타입 힌트

```python
def add(a: float, b: float) -> float:
    """타입 힌트로 명확한 인터페이스"""
    return a + b
```

### Docstring

```python
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
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b
```

### 예외 처리

```python
def test_divide_by_zero():
    """0으로 나누면 예외 발생"""
    with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
        divide(10, 0)
```

## 📊 테스트 통계

- **총 테스트**: 25개
- **기본 연산 테스트**: 16개
- **추가 함수 테스트**: 5개
- **통합 테스트**: 2개
- **Edge Case 테스트**: 2개

## 🎓 학습 포인트

### 1. TDD 사이클

각 함수는 Red-Green-Refactor를 거쳤습니다:
1. 🔴 테스트 작성 → 실패 확인
2. 🟢 최소 구현 → 통과 확인
3. 🔵 리팩토링 → 개선

### 2. 점진적 개선

```python
# Green: 최소 구현
def add(a, b):
    return a + b

# Refactor: 타입 힌트
def add(a: float, b: float) -> float:
    return a + b

# Refactor: Docstring
def add(a: float, b: float) -> float:
    """두 숫자를 더합니다."""
    return a + b
```

### 3. 테스트의 가치

- 버그 조기 발견
- 안전한 리팩토링
- 명확한 요구사항
- 코드 문서 역할

## 🔗 비교 학습

### 자신의 코드와 비교

1. **구조 비교**: 함수 구조가 비슷한가?
2. **테스트 범위**: 어떤 케이스를 놓쳤나?
3. **코드 품질**: 타입 힌트, docstring이 있는가?
4. **예외 처리**: Edge case를 고려했는가?

### 개선 아이디어

- [ ] 더 많은 테스트 케이스 추가
- [ ] 다른 연산 함수 추가 (제곱근, 절댓값 등)
- [ ] 복잡한 계산기 기능 (수식 파싱)
- [ ] 계산 히스토리 기능

## 💬 더 배우기

이 모범 답안은 한 가지 방법일 뿐입니다:
- 다른 방식으로도 구현 가능
- 더 나은 방법이 있을 수 있음
- 본인만의 스타일 개발 권장

---

**참고**: 이 답안을 보기 전에 먼저 직접 해보세요!
실패와 시행착오가 가장 좋은 학습입니다.
