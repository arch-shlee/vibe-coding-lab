# Starter - Red-Green-Refactor 심화

> TDD로 고급 계산기를 구현하는 시작 템플릿입니다.

## 📂 파일 구조

```
starter/
├── README.md           # 이 파일
├── calculator.py       # 계산기 구현 (여기에 코드 작성)
├── test_calculator.py  # 테스트 작성 (여기에 테스트 작성)
└── requirements.txt    # 의존성
```

---

## 🚀 시작하기

### 1. 환경 설정

```bash
# 가상 환경 생성 (선택)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 테스트 실행

```bash
# 모든 테스트 실행
pytest test_calculator.py -v

# 특정 테스트만
pytest test_calculator.py::test_두_숫자_덧셈 -v

# 커버리지와 함께
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

---

## 🎯 미션

### 목표

문자열 수식을 계산하는 계산기를 **TDD**로 구현하세요.

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
calculate("2 + 3 + 4")   # 9
calculate("10 - 2 + 3")  # 11
```

#### Phase 3: 연산자 우선순위
```python
calculate("2 + 3 * 4")   # 14 (곱셈 먼저!)
calculate("10 - 6 / 3")  # 8.0
```

#### Phase 4: 괄호 (선택)
```python
calculate("(2 + 3) * 4") # 20
```

#### Phase 5: Edge Cases
```python
calculate("10 / 0")      # ZeroDivisionError
calculate("2 +")         # ValueError
calculate("")            # ValueError
```

---

## 📝 TDD 사이클

**모든 기능**을 다음 순서로 개발하세요:

### 🔴 Red (빨강)
1. `test_calculator.py`에 테스트 작성
2. 테스트 실행 → 실패 확인 (빨간불)

### 🟢 Green (초록)
3. `calculator.py`에 최소한의 코드 작성
4. 테스트 실행 → 통과 확인 (초록불)

### 🔵 Refactor (파랑)
5. 코드 개선 (중복 제거, 구조 정리)
6. 테스트 실행 → 여전히 통과 확인

---

## 💡 개발 가이드

### 순서 제안

1. **가장 간단한 것부터**
   ```python
   # test_calculator.py
   def test_두_숫자_덧셈():
       result = calculate("2 + 3")
       assert result == 5
   ```

2. **삼각측량**
   ```python
   def test_다른_숫자_덧셈():
       result = calculate("10 + 7")
       assert result == 17
   ```

3. **다른 연산 추가**
   - 뺄셈 → 곱셈 → 나눗셈

4. **리팩토링**
   - 중복 제거
   - 함수 분리

5. **복잡한 기능**
   - 여러 연산 → 우선순위 → 괄호

### AI 활용 팁

**효과적인 프롬프트 예시**:
```
test_calculator.py에 덧셈 테스트를 작성했어.

calculator.py에 calculate 함수를 구현해줘.

요구사항:
- 문자열을 파싱해서 계산
- "2 + 3" 형식 지원
- split() 메서드 사용

최소한의 코드로 작성해줘.
```

---

## 🎓 체크리스트

각 Phase를 완료할 때마다 체크하세요:

### Phase 1: 기본 연산
- [ ] 덧셈 테스트 작성 및 통과
- [ ] 뺄셈 테스트 작성 및 통과
- [ ] 곱셈 테스트 작성 및 통과
- [ ] 나눗셈 테스트 작성 및 통과
- [ ] 코드 리팩토링 완료
- [ ] Red-Green-Refactor 사이클을 따랐다

### Phase 2: 복합 연산
- [ ] 여러 덧셈 테스트 및 통과
- [ ] 혼합 연산 테스트 및 통과
- [ ] 함수 분리 (필요시)

### Phase 3: 우선순위
- [ ] 곱셈 우선순위 테스트 및 통과
- [ ] 나눗셈 우선순위 테스트 및 통과
- [ ] 복잡한 수식 테스트 및 통과

### Phase 4: 괄호 (선택)
- [ ] 단일 괄호 테스트 및 통과
- [ ] 중첩 괄호 테스트 및 통과

### Phase 5: Edge Cases
- [ ] 0으로 나누기 예외 처리
- [ ] 잘못된 입력 예외 처리
- [ ] 빈 문자열 예외 처리

---

## 🆘 막혔나요?

### 가이드 문서
- [GUIDE.md](../GUIDE.md): 완전한 단계별 가이드
- [checkpoints/](../checkpoints/): 진행 상황 점검

### AI에게 질문하기

막혔을 때:
1. 에러 메시지를 AI에게 보여주기
2. 지금까지 작성한 코드 공유
3. 어떤 부분이 어려운지 설명

### Solution (최후의 수단)
- [../solution/](../solution/): 막힐 때만 참고
- 전체를 복사하지 말고 힌트만 얻기

---

## 🎯 학습 목표

이 실습을 완료하면:

- ✅ 복잡한 로직을 TDD로 구현하는 방법 체득
- ✅ 리팩토링 타이밍 판단 능력 향상
- ✅ Edge case 발견 및 처리 능력 향상
- ✅ AI와 효과적으로 협업하는 방법 습득

---

**Happy TDD! 🚀**

*"테스트를 먼저 작성하면, 두려움 없이 코드를 작성할 수 있습니다." - Kent Beck*
