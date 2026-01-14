# 02-first-tdd: 실습 폴더

> TDD를 직접 경험해보세요!

## 📂 파일 구조

이 폴더에서 다음 파일들을 작성하게 됩니다:

```
starter/
├── README.md            # 이 파일
├── calculator.py        # 계산기 함수 구현
├── test_calculator.py   # 계산기 테스트
├── string_utils.py      # 도전 과제: 문자열 유틸리티
└── test_string_utils.py # 도전 과제: 문자열 테스트
```

## 🚀 시작하기

### 1. pytest 설치 확인

```bash
pytest --version

# 설치 안 되어 있다면
pip install pytest
```

### 2. GUIDE.md 따라하기

[../GUIDE.md](../GUIDE.md)를 열고 단계별로 따라하세요.

## 💡 실습 순서

### Part 1: 덧셈 (add)

1. `test_calculator.py`에 테스트 작성
2. pytest 실행 → 🔴 실패 확인
3. `calculator.py`에 함수 작성
4. pytest 실행 → 🟢 통과 확인
5. 리팩토링 (타입 힌트, docstring)

### Part 2-4: 뺄셈, 곱셈, 나눗셈

같은 방식으로 반복:
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

### Part 5: Edge Cases

- 0으로 나누기 예외 처리
- 음수 처리
- 소수점 처리

## ✅ 테스트 실행

### 모든 테스트 실행

```bash
pytest test_calculator.py -v
```

### 특정 테스트만

```bash
pytest test_calculator.py::test_add_two_positive_numbers -v
```

### 상세 출력

```bash
pytest test_calculator.py -vv
```

## 🎯 완료 기준

- [ ] calculator.py에 4개 함수 작성 (add, subtract, multiply, divide)
- [ ] test_calculator.py에 테스트 7개 이상 작성
- [ ] 모든 테스트 통과 (🟢)
- [ ] 0으로 나누기 예외 처리
- [ ] 각 함수에 타입 힌트와 docstring 추가

## 💁 도움말

### AI에게 도움 요청하기

**테스트 작성**:
```
"pytest로 add 함수를 테스트하는 코드를 작성해줘.
2 + 3 = 5를 검증하는 테스트야."
```

**함수 구현**:
```
"test_add_two_positive_numbers 테스트를 통과하는
가장 간단한 add 함수를 작성해줘."
```

**리팩토링**:
```
"add 함수에 타입 힌트와 docstring을 추가해줘."
```

### 막혔을 때

1. GUIDE.md의 예제 코드 참고
2. AI에게 질문하기
3. `../solution/` 폴더 참고 (마지막 수단)

## 🎉 완료 후

- [../checkpoints/](../checkpoints/)에서 진행 상황 확인
- [../../03-ai-assistant/](../../03-ai-assistant/)로 이동

---

**Happy TDD! 🚀**
