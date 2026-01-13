# 01-hello-vibe: 모범 답안

> 실습이 막힐 때만 참고하세요!

## 📂 파일 설명

### hello.py
가장 간단한 Python 프로그램입니다.
- `print()` 함수로 문자열 출력
- 프로그래밍의 전통적인 첫 프로그램

### hello_personal.py
사용자 입력을 받는 프로그램입니다.
- `input()` 함수로 사용자 입력 받기
- f-string으로 문자열 포맷팅
- 변수에 값 저장하고 사용하기

### calculator.py
함수를 정의하고 사용하는 프로그램입니다.
- 함수 정의: `def 함수명(매개변수):`
- Docstring으로 함수 설명
- 함수 호출 및 반환값 사용
- `if __name__ == "__main__":` 패턴

### list_sum.py
리스트를 처리하는 프로그램입니다.
- 리스트 순회: `for ... in ...`
- 누적 합산 패턴
- Python 내장 함수 활용
- 여러 구현 방법 비교

## 💡 학습 포인트

### 1. 코드 구조
모든 코드는 다음 구조를 따릅니다:
```python
"""
파일 설명 (Docstring)
"""

# 함수 정의
def 함수명(매개변수):
    """함수 설명"""
    # 구현
    return 결과

# 테스트 코드
if __name__ == "__main__":
    # 함수 실행 및 결과 확인
```

### 2. 주석의 중요성
- 파일 상단에 Docstring으로 전체 설명
- 함수마다 Docstring으로 기능 설명
- 복잡한 로직에 인라인 주석

### 3. 테스트 패턴
각 파일은 실행 가능하도록 테스트 코드를 포함합니다:
```python
if __name__ == "__main__":
    # 여기서 함수 테스트
```

## 🔍 코드 비교

### 여러 가지 구현 방법

**리스트 합산 - 방법 1 (반복문)**:
```python
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

**리스트 합산 - 방법 2 (내장 함수)**:
```python
def sum_list(numbers):
    return sum(numbers)
```

**리스트 합산 - 방법 3 (reduce)**:
```python
from functools import reduce

def sum_list(numbers):
    return reduce(lambda x, y: x + y, numbers, 0)
```

모두 같은 결과지만, 방법 2가 가장 Pythonic합니다!

## ✅ 실행 결과

### hello.py
```bash
$ python hello.py
Hello, World!
```

### hello_personal.py
```bash
$ python hello_personal.py
이름을 입력하세요: Alice
Hello, Alice!
```

### calculator.py
```bash
$ python calculator.py
3 + 5 = 8
10 + 20 = 30
첫 번째 숫자를 입력하세요: 7
두 번째 숫자를 입력하세요: 3
7.0 + 3.0 = 10.0
```

### list_sum.py
```bash
$ python list_sum.py
리스트 [1, 2, 3, 4, 5]의 합: 15
리스트 [10, 20, 30, 40]의 합: 100
내장 함수 사용: 15
빈 리스트의 합: 0
```

## 🎓 학습 정리

### 배운 개념들

1. **기본 출력**: `print()`
2. **사용자 입력**: `input()`
3. **변수**: 값 저장 및 재사용
4. **함수**: `def`로 정의, 매개변수, 반환값
5. **Docstring**: `"""`로 문서화
6. **리스트**: 여러 값을 저장
7. **반복문**: `for ... in ...`
8. **조건문**: `if __name__ == "__main__":`
9. **문자열 포맷팅**: f-string

### 다음 단계

이 모듈을 완료했다면:
- 각 코드를 직접 타이핑해보세요 (복사-붙여넣기 대신)
- 코드를 조금씩 수정해보며 실험하세요
- AI에게 "이 코드를 설명해줘"라고 요청해보세요

---

**참고**: 이 답안은 한 가지 방법일 뿐입니다. 여러분의 코드가 다르더라도 작동한다면 정답입니다!
