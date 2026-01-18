# Solution - Todo List 앱 모범 답안

> TDD로 개발한 Todo List 앱의 완성된 구현입니다.

## ⚠️ 중요한 안내

### 이 폴더를 보기 전에...

**Solution은 최후의 수단입니다!**

1. ✅ **먼저 스스로 시도하세요**
   - GUIDE.md를 따라 직접 구현
   - AI와 협업하며 문제 해결

2. ✅ **막혔을 때 체크포인트 확인**
   - checkpoints/에서 진행 상황 점검
   - 어느 부분에서 막혔는지 파악

3. ✅ **특정 부분만 참고하세요**
   - 전체를 복사하지 말고
   - 막힌 부분의 힌트만 얻기

4. ⚠️ **Solution을 보는 이유 기록**
   - 왜 막혔는지
   - Solution을 보고 무엇을 배웠는지
   - 다음에는 어떻게 할지

---

## 📂 파일 구조

```
solution/
├── README.md           # 이 파일
├── todo_list.py        # 완성된 TodoList 클래스
├── test_todo_list.py   # 완성된 테스트 스위트
└── requirements.txt    # 의존성 목록
```

---

## 🎯 구현 완료 기능

### 핵심 기능
- ✅ Todo 추가 (add)
- ✅ Todo 조회 (get_all)
- ✅ Todo 완료 (complete)
- ✅ Todo 삭제 (delete)

### 추가 기능 (보너스)
- ✅ ID로 조회 (get_by_id)
- ✅ 완료된 Todo만 조회 (get_completed)
- ✅ 미완료 Todo만 조회 (get_incomplete)

---

## 🧪 테스트 실행

```bash
# 이 폴더(solution)에서 실행

# 의존성 설치
pip install -r requirements.txt

# 모든 테스트 실행
pytest test_todo_list.py -v

# 커버리지와 함께 실행
pytest test_todo_list.py --cov=todo_list --cov-report=term-missing

# 특정 테스트만 실행
pytest test_todo_list.py::test_todo_추가 -v
```

### 예상 결과

```
test_todo_list.py::test_todo_list_초기화 PASSED
test_todo_list.py::test_todo_추가 PASSED
test_todo_list.py::test_여러_todo_추가 PASSED
...
======================== 25 passed in 0.05s =========================

---------- coverage: platform darwin, python 3.11.0 -----------
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
todo_list.py        45      0   100%
----------------------------------------------
TOTAL               45      0   100%
```

---

## 📚 구현 설명

### 클래스 설계

```python
class TodoList:
    def __init__(self):
        self._todos: Dict[int, Dict] = {}
        self._next_id: int = 1
```

**핵심 결정 사항**:
- `_todos`: 딕셔너리 사용 (ID로 빠른 접근)
- `_next_id`: 자동 증가 ID 관리

### 메서드별 특징

#### add(title: str) → Dict
```python
def add(self, title: str) -> Dict:
    if not title or not title.strip():
        raise ValueError("할 일 제목은 비어있을 수 없습니다")
    # ...
```

**포인트**:
- 입력 검증 (빈 문자열, 공백)
- 타입 힌트 사용
- 명확한 에러 메시지

#### get_all() → List[Dict]
```python
def get_all(self) -> List[Dict]:
    return list(self._todos.values())
```

**포인트**:
- 간단하고 명확한 구현
- 딕셔너리 values를 리스트로 변환

#### complete(todo_id: int) → Dict
```python
def complete(self, todo_id: int) -> Dict:
    if todo_id not in self._todos:
        raise KeyError(f"ID {todo_id}인 할 일을 찾을 수 없습니다")
    # ...
```

**포인트**:
- 존재 여부 검증
- 명확한 에러 메시지 (f-string 사용)

#### delete(todo_id: int) → bool
```python
def delete(self, todo_id: int) -> bool:
    if todo_id not in self._todos:
        raise KeyError(f"ID {todo_id}인 할 일을 찾을 수 없습니다")
    del self._todos[todo_id]
    return True
```

**포인트**:
- 예외 처리 후 삭제
- 성공 시 True 반환

---

## 🧪 테스트 전략

### 테스트 구조

```python
# Given-When-Then 패턴
def test_todo_추가():
    # Given: 준비
    todo_list = TodoList()

    # When: 실행
    result = todo_list.add("Python 공부하기")

    # Then: 검증
    assert result["id"] == 1
    assert result["title"] == "Python 공부하기"
```

### 테스트 카테고리

1. **정상 케이스**: 기능이 제대로 작동하는지
2. **예외 케이스**: 잘못된 입력 처리
3. **엣지 케이스**: 경계 조건 (빈 리스트, 공백 등)
4. **통합 테스트**: 여러 기능 조합

### 커버리지 100%

모든 코드 라인이 테스트됩니다:
- 모든 메서드
- 모든 분기 (if/else)
- 모든 예외 처리

---

## 💡 주요 배울 점

### 1. TDD의 가치

**Before TDD**:
```python
# 코드 먼저 작성 → 나중에 테스트 → 테스트가 귀찮음 → 안 함
def add(self, title):
    self._todos[self._next_id] = {"title": title}
    self._next_id += 1
```

**After TDD**:
```python
# 테스트 먼저 → 요구사항 명확 → 자신감 있는 코드
def test_빈_문자열_추가_실패():  # 먼저 요구사항 정의
    with pytest.raises(ValueError):
        todo_list.add("")

def add(self, title):  # 그 다음 구현
    if not title or not title.strip():
        raise ValueError("...")
```

### 2. 명확한 에러 메시지

**나쁜 예**:
```python
raise KeyError("Not found")  # 뭐가 없다는 거지?
```

**좋은 예**:
```python
raise KeyError(f"ID {todo_id}인 할 일을 찾을 수 없습니다")
```

### 3. 타입 힌트의 중요성

```python
def add(self, title: str) -> Dict:  # 입력과 출력이 명확
    ...
```

- 코드 가독성 향상
- IDE 자동완성 지원
- 버그 조기 발견

### 4. Docstring 작성

```python
def complete(self, todo_id: int) -> Dict:
    """
    할 일을 완료 처리합니다.

    Args:
        todo_id: 완료할 todo의 ID

    Returns:
        완료 처리된 todo 객체

    Raises:
        KeyError: 해당 ID의 todo가 존재하지 않는 경우
    """
```

Google 스타일 docstring으로:
- 무엇을 하는지
- 파라미터 설명
- 반환값 설명
- 예외 상황

---

## 🔄 개선 가능한 부분

이 구현은 완벽하지 않습니다. 개선할 수 있는 부분들:

### 1. 데이터 영속성
현재는 메모리에만 저장됩니다.

**개선안**:
- JSON 파일로 저장/불러오기
- 데이터베이스 연동 (SQLite)

### 2. Todo 수정 기능
```python
def update(self, todo_id: int, title: str) -> Dict:
    """Todo 제목을 수정"""
    # 구현하기
```

### 3. Todo 정렬
```python
def get_all(self, sort_by: str = "id") -> List[Dict]:
    """정렬 옵션 추가: id, title, completed"""
    # 구현하기
```

### 4. 더 풍부한 Todo 정보
```python
{
    "id": 1,
    "title": "...",
    "completed": False,
    "created_at": "2026-01-18 10:00:00",  # 생성 시간
    "due_date": "2026-01-20",              # 마감일
    "priority": "high"                     # 우선순위
}
```

---

## 📊 성능 분석

### 시간 복잡도

| 메서드 | 시간 복잡도 | 설명 |
|--------|-------------|------|
| add | O(1) | 딕셔너리 삽입 |
| get_all | O(n) | 모든 항목 조회 |
| complete | O(1) | 딕셔너리 접근 |
| delete | O(1) | 딕셔너리 삭제 |

### 공간 복잡도

O(n) - n은 todo 개수

---

## 🎓 다음 학습 과제

이 Solution을 이해했다면:

1. **직접 구현해보기**
   - Solution을 보지 않고
   - TDD로 처음부터 다시 구현

2. **확장 기능 추가**
   - 위의 "개선 가능한 부분" 구현
   - 자신만의 기능 추가

3. **다른 언어로 구현**
   - JavaScript로 똑같은 기능
   - TypeScript로 타입 안전하게

4. **Level 2로 진행**
   - 더 복잡한 프로젝트
   - 고급 TDD 기법

---

## 💬 Solution 활용 팁

### ✅ 좋은 활용법

1. **비교 학습**
   - 내 코드와 비교
   - 어떤 점이 다른지 분석

2. **부분 참고**
   - 막힌 메서드만 확인
   - 힌트만 얻고 직접 작성

3. **테스트 아이디어**
   - 어떤 테스트가 필요한지 확인
   - 내 프로젝트에 적용

### ❌ 피해야 할 사용법

1. **전체 복사-붙여넣기**
   - 배우는 것이 없음
   - 실력 향상 안 됨

2. **이해 없이 넘어가기**
   - 왜 이렇게 했는지 이해 필수
   - 질문하고 실험하기

---

## 🆘 궁금한 점이 있나요?

### 코드 관련 질문
- "왜 딕셔너리를 사용했나요?"
- "리스트를 쓰면 안 되나요?"
- "타입 힌트는 꼭 필요한가요?"

**AI에게 물어보세요!**
```
"solution의 todo_list.py에서 딕셔너리를 사용한 이유를 설명해줘.
리스트와 비교해서 장단점도 알려줘."
```

### 커뮤니티
- [GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)
- 다른 학습자들과 토론

---

**이 Solution을 참고하셨다면, 꼭 직접 다시 구현해보세요!**

*"읽는 것과 하는 것은 완전히 다릅니다. 손으로 타이핑하며 배워야 진짜 내 것이 됩니다."*

---

**버전**: 1.0
**작성일**: 2026-01-18
**커버리지**: 100%
**테스트**: 25개 통과
