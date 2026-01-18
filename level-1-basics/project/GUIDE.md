# Todo List 앱 개발 가이드

> TDD로 처음부터 끝까지 Todo List 앱을 만드는 완전한 가이드입니다.

## 📖 이 가이드 사용법

### 가이드 철학

이 가이드는 **물고기를 주는 것이 아니라, 물고기 잡는 법을 알려줍니다**.

- ✅ 각 단계의 **사고 과정**을 보여줍니다
- ✅ **왜** 이렇게 하는지 설명합니다
- ✅ AI에게 **어떻게 요청**하는지 예시를 제공합니다
- ❌ 완성된 코드를 바로 제공하지 않습니다

### 추천 학습 방법

1. **한 단계씩 천천히**: 각 단계를 완전히 이해하고 넘어가세요
2. **직접 코딩**: 복사-붙여넣기보다 직접 타이핑하세요
3. **AI와 대화**: 가이드는 참고만, 실제 구현은 AI와 함께
4. **막히면 solution/**: 정말 막혔을 때만 참고하세요

---

## 🎯 전체 개발 로드맵

### Phase 1: 프로젝트 설정 (15분)
- 환경 설정
- 초기 파일 구조
- 첫 테스트 실행

### Phase 2: Todo 추가 기능 (1시간)
- 테스트 작성
- 최소 구현
- 리팩토링

### Phase 3: Todo 조회 기능 (30분)
- 전체 조회 구현
- 빈 리스트 처리

### Phase 4: Todo 완료 기능 (45분)
- 완료 처리 구현
- 예외 처리

### Phase 5: Todo 삭제 기능 (45분)
- 삭제 구현
- 예외 처리

### Phase 6: 통합 및 리팩토링 (1-2시간)
- 전체 테스트
- 코드 정리
- 문서화

---

## Phase 1: 프로젝트 설정

### Step 1.1: 환경 준비

**목표**: 개발 환경을 설정하고 pytest가 작동하는지 확인

```bash
# starter 폴더로 이동
cd level-1-basics/project/starter

# 가상 환경 생성 (선택사항이지만 권장)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

**확인**:
```bash
pytest --version
# pytest 7.x.x 등이 출력되면 성공
```

### Step 1.2: 초기 파일 구조 이해

`starter/` 폴더에는 다음 파일들이 있습니다:

```
starter/
├── todo_list.py          # 여기에 TodoList 클래스 구현
├── test_todo_list.py     # 여기에 테스트 작성
└── requirements.txt      # 의존성 목록
```

**todo_list.py**를 열어보세요:
```python
# todo_list.py
"""
Todo List 애플리케이션

TDD로 개발하는 간단한 할 일 관리 앱입니다.
"""

class TodoList:
    """할 일 목록을 관리하는 클래스"""

    def __init__(self):
        """TodoList 초기화"""
        pass

    # 여기에 메서드들을 구현하세요
```

**test_todo_list.py**를 열어보세요:
```python
# test_todo_list.py
"""
Todo List 테스트

TDD의 Red-Green-Refactor 사이클을 따라 작성합니다.
"""
import pytest
from todo_list import TodoList

# 여기에 테스트들을 작성하세요
```

### Step 1.3: 첫 테스트 작성 및 실행

**TDD의 첫 단계**: 🔴 Red - 실패하는 테스트 작성

`test_todo_list.py`에 가장 간단한 테스트를 추가하세요:

```python
def test_todo_list_초기화():
    """TodoList를 생성할 수 있어야 함"""
    todo = TodoList()
    assert todo is not None
```

**테스트 실행**:
```bash
pytest test_todo_list.py -v
```

**예상 결과**: 🟢 초록불! (이미 `__init__`이 있으므로)
```
test_todo_list.py::test_todo_list_초기화 PASSED
```

---

## Phase 2: Todo 추가 기능 (TDD 사이클 체험)

이제 본격적으로 TDD 사이클을 경험해봅시다!

### Step 2.1: 🔴 Red - 실패하는 테스트 작성

**생각 과정**:
1. 무엇을 만들까? → Todo를 추가하는 기능
2. 어떻게 사용될까? → `todo.add("할 일 내용")`
3. 결과가 무엇일까? → 추가된 Todo 객체 반환

**AI에게 요청** (안티그라비티):
```
test_todo_list.py에 Todo 추가 기능의 테스트를 작성해줘.

요구사항:
- 메서드 이름: add
- 파라미터: title (문자열)
- 반환값: 생성된 todo 딕셔너리 (id, title, completed 포함)
- 테스트 함수명: test_todo_추가

pytest 형식으로 작성해줘.
```

**AI 응답 예시**:
```python
def test_todo_추가():
    """Todo를 추가할 수 있어야 함"""
    todo_list = TodoList()
    result = todo_list.add("Python 공부하기")

    assert result is not None
    assert result["id"] == 1
    assert result["title"] == "Python 공부하기"
    assert result["completed"] == False
```

**테스트 실행**:
```bash
pytest test_todo_list.py::test_todo_추가 -v
```

**예상 결과**: 🔴 빨간불!
```
AttributeError: 'TodoList' object has no attribute 'add'
```

**축하합니다!** 첫 Red를 경험했습니다. 이제 Green으로!

### Step 2.2: 🟢 Green - 테스트 통과하는 최소 코드

**생각 과정**:
- 테스트를 통과하려면 뭐가 필요할까?
- `add` 메서드 필요
- id, title, completed를 가진 딕셔너리 반환

**AI에게 요청**:
```
todo_list.py에 add 메서드를 구현해줘.

요구사항:
- title을 받아서 todo 추가
- id는 1부터 시작해서 자동 증가
- completed는 기본값 False
- 생성된 todo 딕셔너리 반환

최소한의 코드로 작성해줘.
```

**구현 후 테스트**:
```bash
pytest test_todo_list.py::test_todo_추가 -v
```

**예상 결과**: 🟢 초록불!
```
test_todo_list.py::test_todo_추가 PASSED
```

### Step 2.3: 추가 테스트 케이스

**생각 과정**:
- ID가 정말 자동 증가하나?
- 여러 개를 추가하면 어떻게 되나?

**테스트 추가**:
```python
def test_여러_todo_추가():
    """여러 개의 Todo를 추가하면 ID가 증가해야 함"""
    todo_list = TodoList()

    todo1 = todo_list.add("첫 번째 할 일")
    todo2 = todo_list.add("두 번째 할 일")

    assert todo1["id"] == 1
    assert todo2["id"] == 2
```

**테스트 실행 및 통과 확인**

### Step 2.4: 🔵 Refactor - 코드 개선

테스트가 모두 통과하면 코드를 개선할 시간입니다.

**생각해볼 점**:
- 변수명이 명확한가?
- 주석이 필요한가?
- 중복 코드가 있나?
- 타입 힌트를 추가하면?

**AI에게 요청**:
```
todo_list.py의 add 메서드를 리팩토링해줘.

개선 사항:
- 타입 힌트 추가
- docstring 추가 (Google 스타일, 한글)
- 변수명 개선

테스트는 그대로 통과해야 해.
```

**리팩토링 후 테스트**:
```bash
pytest test_todo_list.py -v
```

**모든 테스트가 여전히 통과**하면 성공!

### Step 2.5: 예외 케이스 처리

**생각 과정**:
- 빈 문자열을 추가하면?
- None을 전달하면?

**테스트 추가**:
```python
def test_빈_문자열_추가_실패():
    """빈 문자열은 추가할 수 없어야 함"""
    todo_list = TodoList()

    with pytest.raises(ValueError):
        todo_list.add("")
```

**🔴 Red → 🟢 Green → 🔵 Refactor 반복!**

---

## Phase 3: Todo 조회 기능

### Step 3.1: 전체 조회 기능 계획

**생각 과정**:
1. 메서드 이름: `get_all()`
2. 반환값: 모든 todo 리스트
3. 빈 리스트도 처리해야 함

### Step 3.2: 🔴 Red - 테스트 작성

**AI에게 요청**:
```
test_todo_list.py에 전체 조회 테스트를 작성해줘.

테스트 케이스:
1. 빈 리스트 조회
2. todo를 추가한 후 조회
3. 여러 todo를 추가한 후 조회

메서드 이름: get_all
```

### Step 3.3: 🟢 Green - 구현

**AI에게 요청**:
```
todo_list.py에 get_all 메서드를 구현해줘.

요구사항:
- 모든 todo를 리스트로 반환
- 빈 리스트인 경우 빈 배열 반환
```

### Step 3.4: 🔵 Refactor - 개선

코드 정리 및 문서화

---

## Phase 4: Todo 완료 기능

### Step 4.1: 완료 기능 계획

**생각 과정**:
1. 메서드 이름: `complete(id)`
2. 동작: id에 해당하는 todo의 completed를 True로
3. 반환값: 완료된 todo 객체
4. 예외: 존재하지 않는 id

### Step 4.2: 🔴 Red - 테스트 작성

**테스트 케이스**:
```python
def test_todo_완료():
    """Todo를 완료 처리할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("운동하기")

    result = todo_list.complete(1)

    assert result["id"] == 1
    assert result["completed"] == True


def test_존재하지_않는_todo_완료_실패():
    """존재하지 않는 ID는 예외 발생"""
    todo_list = TodoList()

    with pytest.raises(KeyError):
        todo_list.complete(999)
```

### Step 4.3: 🟢 Green - 구현

**AI에게 요청**:
```
todo_list.py에 complete 메서드를 구현해줘.

요구사항:
- id를 받아서 해당 todo의 completed를 True로
- 존재하지 않는 id면 KeyError 발생
- 완료된 todo 객체 반환
```

### Step 4.4: 🔵 Refactor

---

## Phase 5: Todo 삭제 기능

### Step 5.1: 삭제 기능 계획

**생각 과정**:
1. 메서드 이름: `delete(id)`
2. 동작: id에 해당하는 todo 제거
3. 반환값: True (성공)
4. 예외: 존재하지 않는 id

### Step 5.2: 🔴 Red - 테스트 작성

**AI에게 요청하세요!** (패턴을 이제 아시죠?)

### Step 5.3: 🟢 Green - 구현

### Step 5.4: 🔵 Refactor

---

## Phase 6: 통합 및 리팩토링

### Step 6.1: 전체 테스트 실행

```bash
# 모든 테스트 실행
pytest test_todo_list.py -v

# 커버리지 확인
pytest test_todo_list.py --cov=todo_list --cov-report=term-missing
```

**목표**: 모든 테스트 통과, 커버리지 80% 이상

### Step 6.2: 코드 리뷰

**AI에게 요청**:
```
todo_list.py 코드를 리뷰해줘.

체크 포인트:
- 코드 가독성
- 변수/함수 이름
- 주석 및 문서화
- DRY 원칙
- 예외 처리

개선 제안을 해줘.
```

### Step 6.3: 최종 리팩토링

**개선 포인트**:
- [ ] 반복되는 코드 제거
- [ ] 명확한 에러 메시지
- [ ] 일관된 코딩 스타일
- [ ] 완전한 docstring

### Step 6.4: 통합 테스트 추가

**시나리오 테스트**:
```python
def test_전체_시나리오():
    """실제 사용 시나리오 테스트"""
    todo_list = TodoList()

    # 할 일 3개 추가
    todo_list.add("아침 운동")
    todo_list.add("Python 공부")
    todo_list.add("저녁 독서")

    # 하나 완료
    todo_list.complete(2)

    # 하나 삭제
    todo_list.delete(1)

    # 최종 확인
    todos = todo_list.get_all()
    assert len(todos) == 2
    assert todos[0]["title"] == "Python 공부"
    assert todos[0]["completed"] == True
```

---

## 🎯 체크리스트

### 기능 완성도
- [ ] Todo 추가 기능 작동
- [ ] Todo 조회 기능 작동
- [ ] Todo 완료 기능 작동
- [ ] Todo 삭제 기능 작동
- [ ] 모든 예외 처리 완료

### 테스트
- [ ] 모든 테스트 통과
- [ ] 커버리지 80% 이상
- [ ] 예외 케이스 테스트 포함
- [ ] 통합 시나리오 테스트 포함

### 코드 품질
- [ ] 명확한 함수/변수 이름
- [ ] 모든 함수에 docstring
- [ ] 타입 힌트 추가
- [ ] DRY 원칙 준수

### TDD 실천
- [ ] Red-Green-Refactor 사이클 따름
- [ ] 테스트 먼저 작성
- [ ] 커밋 메시지 명확

---

## 💡 학습 팁

### AI와 효과적으로 협업하기

**좋은 프롬프트 예시**:
```
✅ "test_todo_list.py에 Todo 삭제 기능의 테스트를 작성해줘.
   - 정상 삭제 케이스
   - 존재하지 않는 ID 예외 케이스
   - 삭제 후 목록에서 제거 확인
   pytest 형식으로 작성해줘."
```

**나쁜 프롬프트 예시**:
```
❌ "todo 앱 만들어줘"
❌ "테스트 작성해줘"
```

### 막혔을 때 대처법

1. **AI에게 설명 요청**
   ```
   "이 코드가 왜 작동하지 않는지 설명해줘"
   ```

2. **에러 메시지 공유**
   ```
   "이런 에러가 나는데 어떻게 해결하나요?
   [에러 메시지 붙여넣기]"
   ```

3. **단계별 요청**
   ```
   "complete 메서드를 단계별로 구현하는 방법을 알려줘"
   ```

4. **solution/ 참고** (최후의 수단)

---

## 🎓 다음 단계

### 추가 도전 과제

프로젝트를 완료했다면:

#### 레벨 1: 기능 확장
- [ ] Todo 수정 기능 (update)
- [ ] 완료/미완료 필터링
- [ ] Todo 개수 세기

#### 레벨 2: 고급 기능
- [ ] Todo 카테고리
- [ ] 우선순위 설정
- [ ] 마감일 추가

#### 레벨 3: 영속성
- [ ] JSON 파일로 저장/불러오기
- [ ] CSV export
- [ ] 데이터베이스 연동 (SQLite)

### 학습 정리

프로젝트를 마친 후:

1. **회고록 작성**
   - 무엇을 배웠나요?
   - 어떤 부분이 어려웠나요?
   - 다음에는 어떻게 하겠나요?

2. **GitHub에 공유**
   - 코드 커밋
   - README 작성
   - 다른 학습자와 공유

3. **Level 2로 진행**
   - [Level 2: 중급](../../level-2-intermediate/README.md)

---

## 🆘 FAQ

### Q: 테스트를 먼저 작성하는 게 어색해요
**A**: 처음엔 다들 그래요! 연습하면 자연스러워집니다. "이 기능이 어떻게 사용될까?"를 먼저 생각하는 습관을 들이세요.

### Q: AI가 너무 복잡한 코드를 만들어요
**A**: "더 간단하게 만들어줘. 초보자도 이해할 수 있게"라고 요청하세요.

### Q: 테스트가 실패하는데 이유를 모르겠어요
**A**: 에러 메시지를 천천히 읽어보세요. 그래도 모르면 AI에게 에러 메시지를 보여주고 물어보세요.

### Q: solution 코드와 다른데 괜찮나요?
**A**: 완전히 괜찮습니다! 정답은 하나가 아닙니다. 테스트만 통과하면 됩니다.

---

**작성일**: 2026-01-18
**버전**: 1.0
**업데이트**: 학습자 피드백을 반영하여 지속적으로 개선됩니다.
