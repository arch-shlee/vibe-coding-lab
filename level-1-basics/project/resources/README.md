# Resources - 참고 자료

> Todo List 프로젝트에 도움이 되는 추가 학습 자료와 참고 문서입니다.

## 📚 핵심 개념 복습

### TDD (Test-Driven Development)

#### Red-Green-Refactor 사이클
```
🔴 Red: 실패하는 테스트 작성
   ↓
🟢 Green: 테스트를 통과하는 최소 코드
   ↓
🔵 Refactor: 코드 개선
   ↓
   🔄 반복
```

#### TDD의 장점
1. **버그 조기 발견**: 테스트가 요구사항을 정의
2. **자신감 있는 리팩토링**: 테스트가 안전망 역할
3. **더 나은 설계**: 테스트 가능한 코드 = 좋은 설계
4. **문서화**: 테스트가 곧 사용 설명서

### pytest 기본

#### 테스트 함수 작성
```python
def test_기능명():
    """무엇을 테스트하는지 설명"""
    # Given: 준비
    # When: 실행
    # Then: 검증
    assert 조건
```

#### 자주 쓰는 assert
```python
# 같은지 확인
assert result == expected

# 참/거짓 확인
assert condition is True
assert condition is False

# 포함 여부
assert item in collection

# 타입 확인
assert isinstance(value, int)

# 예외 확인
with pytest.raises(ValueError):
    function_that_raises()
```

#### 테스트 실행 옵션
```bash
# 모든 테스트 실행
pytest test_file.py

# 상세 모드 (-v)
pytest test_file.py -v

# 특정 테스트만
pytest test_file.py::test_function_name

# 키워드로 필터링
pytest test_file.py -k "추가"

# 커버리지와 함께
pytest test_file.py --cov=module_name --cov-report=term-missing

# 실패한 테스트만 재실행
pytest test_file.py --lf

# 마지막 실패부터 실행
pytest test_file.py --ff
```

---

## 🐍 Python 클래스 설계

### 클래스 기본
```python
class TodoList:
    """클래스 docstring"""

    def __init__(self):
        """생성자: 인스턴스 초기화"""
        self.속성 = 값

    def 메서드(self, 파라미터):
        """메서드 docstring"""
        # 구현
        return 결과
```

### 타입 힌트
```python
from typing import Dict, List

def add(self, title: str) -> Dict:
    """
    Args:
        title: 할 일 제목 (str)

    Returns:
        생성된 todo (Dict)
    """
    pass

def get_all(self) -> List[Dict]:
    """Returns: 모든 todo 리스트"""
    pass
```

### Docstring 스타일 (Google Style)
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

    Examples:
        >>> todo_list = TodoList()
        >>> todo_list.add("운동하기")
        >>> todo_list.complete(1)
        {'id': 1, 'title': '운동하기', 'completed': True}
    """
    pass
```

---

## 🤖 AI 프롬프트 예시

### 효과적인 프롬프트 작성법

#### ✅ 좋은 프롬프트 예시

**테스트 작성 요청**:
```
test_todo_list.py에 Todo 추가 기능의 테스트를 작성해줘.

테스트 케이스:
1. 정상적으로 Todo를 추가할 수 있다
2. 여러 개 추가 시 ID가 자동 증가한다
3. 빈 문자열은 ValueError 발생

메서드명: add(title: str) -> Dict
반환 형식: {"id": int, "title": str, "completed": bool}

pytest 형식으로, 한글 함수명 사용해줘.
```

**구현 요청**:
```
todo_list.py에 add 메서드를 구현해줘.

요구사항:
- title을 받아서 todo 추가
- id는 1부터 시작해서 자동 증가
- completed는 기본값 False
- 빈 문자열이면 ValueError 발생
- 생성된 todo 딕셔너리 반환

타입 힌트와 docstring(Google 스타일, 한글) 포함해줘.
```

**리팩토링 요청**:
```
todo_list.py의 add 메서드를 리팩토링해줘.

개선 사항:
- 변수명 명확하게
- 주석 추가 (필요한 곳만)
- 에러 메시지 명확하게
- DRY 원칙 적용

테스트는 그대로 통과해야 해.
```

**코드 리뷰 요청**:
```
todo_list.py 코드를 리뷰해줘.

체크 포인트:
- 코드 가독성
- 변수/함수 이름
- 예외 처리
- 타입 힌트
- docstring

개선할 점을 구체적으로 제안해줘.
```

#### ❌ 나쁜 프롬프트 예시
```
❌ "todo 앱 만들어줘"
   → 너무 막연함

❌ "테스트 좀 작성해줘"
   → 어떤 기능인지 불명확

❌ "코드 좀 고쳐줘"
   → 무엇을 어떻게 고칠지 명확하지 않음

❌ "에러 나는데 왜 그래?"
   → 에러 메시지를 공유해야 함
```

### 단계별 프롬프트 전략

#### Phase 1: 이해하기
```
"Todo List 앱을 TDD로 만들려고 해.
먼저 어떤 기능들이 필요한지,
어떤 순서로 개발하면 좋을지 알려줘."
```

#### Phase 2: 설계하기
```
"TodoList 클래스의 구조를 설계하려고 해.
필요한 속성과 메서드를 제안해줘.
각각의 역할도 설명해줘."
```

#### Phase 3: 테스트 작성
```
"add 기능의 테스트를 작성해줘.
정상 케이스와 예외 케이스를 모두 포함해서."
```

#### Phase 4: 구현
```
"test_todo_추가 테스트를 통과하는
add 메서드를 구현해줘."
```

#### Phase 5: 리팩토링
```
"add 메서드를 리팩토링해줘.
타입 힌트, docstring, 에러 메시지 개선."
```

---

## 🔧 유용한 도구

### pytest 플러그인

#### pytest-cov (커버리지)
```bash
# 설치
pip install pytest-cov

# 사용
pytest --cov=todo_list --cov-report=term-missing
pytest --cov=todo_list --cov-report=html  # HTML 리포트
```

#### pytest-watch (자동 실행)
```bash
# 설치
pip install pytest-watch

# 사용: 파일 변경 시 자동으로 테스트 실행
ptw test_todo_list.py
```

### 코드 품질 도구

#### Black (코드 포매터)
```bash
# 설치
pip install black

# 사용
black todo_list.py  # 자동 포맷팅
black --check todo_list.py  # 체크만
```

#### pylint (코드 분석)
```bash
# 설치
pip install pylint

# 사용
pylint todo_list.py
```

#### mypy (타입 체킹)
```bash
# 설치
pip install mypy

# 사용
mypy todo_list.py
```

---

## 📖 추천 학습 자료

### 책

#### TDD 관련
- **"Test Driven Development: By Example"** - Kent Beck
  - TDD의 바이블
  - 실전 예제로 배우기

- **"Growing Object-Oriented Software, Guided by Tests"**
  - 객체지향과 TDD의 조화

#### Python 관련
- **"Fluent Python"** - Luciano Ramalho
  - Python 중급 이상
  - 깊이 있는 Python 이해

- **"Effective Python"** - Brett Slatkin
  - Python 베스트 프랙티스

### 온라인 강의

#### TDD
- [TDD 강의 - 코드스쿼드](https://codesquad.kr)
- [Test-Driven Development - Coursera](https://coursera.org)

#### Python
- [Python 공식 튜토리얼](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com)

### 유튜브

#### 한국어
- **딩코딩코**: 아규먼티드 코딩, TDD
- **노마드 코더**: Python 기초

#### 영어
- **Corey Schafer**: Python 튜토리얼
- **ArjanCodes**: Python 디자인 패턴

---

## 💡 FAQ

### Q1: 테스트를 먼저 작성하는 게 너무 어려워요
**A**:
- 처음엔 다 그래요! 연습이 필요합니다.
- 팁: "이 기능이 어떻게 사용되길 원하는가?"를 먼저 생각하세요.
- 예: `todo.add("할 일")` → 이게 어떻게 작동하길 원하나요?

### Q2: 테스트 커버리지 100%를 목표로 해야 하나요?
**A**:
- 100%가 항상 좋은 건 아닙니다.
- 중요한 비즈니스 로직이 잘 테스트되었는지가 더 중요.
- 80-90%를 목표로 하는 것이 현실적.

### Q3: 모든 예외 케이스를 테스트해야 하나요?
**A**:
- 발생 가능한 예외는 테스트하는 것이 좋습니다.
- 우선순위: 자주 발생할 만한 예외 먼저.

### Q4: AI가 만든 코드를 그대로 써도 되나요?
**A**:
- 절대 그대로 쓰지 마세요!
- 항상 검증하고 이해한 후 사용.
- 이해 안 되면 AI에게 설명 요청.

### Q5: solution과 내 코드가 다른데 괜찮나요?
**A**:
- 완전히 괜찮습니다!
- 정답은 여러 개입니다.
- 중요한 건: 테스트 통과, 요구사항 충족.

---

## 🎯 실전 팁

### TDD 실천 팁

1. **작게 시작하기**
   - 한 번에 하나의 테스트만
   - 가장 간단한 것부터

2. **빨리 피드백 받기**
   - 자주 테스트 실행
   - 오래 기다리지 않기

3. **리팩토링 두려워하지 않기**
   - 테스트가 안전망
   - 초록불이면 마음껏 리팩토링

4. **실패를 확인하기**
   - Red를 실제로 봐야 함
   - 테스트가 제대로 작동하는지 확인

### 디버깅 팁

1. **에러 메시지 잘 읽기**
   ```
   AssertionError: assert 5 == 6
   → 5를 기대했는데 6이 나옴
   ```

2. **print 디버깅**
   ```python
   def add(self, title):
       print(f"title: {title}")  # 디버깅
       print(f"next_id: {self._next_id}")
   ```

3. **pytest -vv 사용**
   ```bash
   pytest test_todo_list.py -vv
   # 더 자세한 출력
   ```

### 협업 팁

1. **명확한 커밋 메시지**
   ```bash
   ❌ git commit -m "fix"
   ✅ git commit -m "test: Todo 추가 테스트 작성"
   ✅ git commit -m "feat: add 메서드 구현"
   ✅ git commit -m "refactor: add 메서드 타입 힌트 추가"
   ```

2. **자주 커밋하기**
   - Red → 커밋
   - Green → 커밋
   - Refactor → 커밋

---

## 🔗 관련 링크

### 공식 문서
- [Python 공식 문서](https://docs.python.org/3/)
- [pytest 공식 문서](https://docs.pytest.org/)
- [typing 모듈](https://docs.python.org/3/library/typing.html)

### 프로젝트 문서
- [프로젝트 개요](../README.md)
- [단계별 가이드](../GUIDE.md)
- [체크포인트](../checkpoints/README.md)
- [모범 답안](../solution/README.md)

### 커뮤니티
- [GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)
- [GitHub Issues](https://github.com/arch-shlee/vibe-coding-lab/issues)

---

## 📝 추가 학습 과제

프로젝트를 완료한 후:

### Level ⭐ - 기본 확장
- [ ] Todo 수정 기능 (`update`)
- [ ] Todo 개수 세기 (`count`)
- [ ] 완료율 계산 (`get_completion_rate`)

### Level ⭐⭐ - 고급 기능
- [ ] Todo 우선순위 (`priority`)
- [ ] 마감일 설정 (`due_date`)
- [ ] Todo 검색 (`search`)
- [ ] 정렬 기능 (`sort_by`)

### Level ⭐⭐⭐ - 영속성
- [ ] JSON 파일 저장/불러오기
- [ ] CSV export
- [ ] SQLite 데이터베이스 연동

### Level ⭐⭐⭐⭐ - 고급 주제
- [ ] CLI 인터페이스 (Click 사용)
- [ ] 웹 API (FastAPI)
- [ ] 웹 인터페이스 (Flask/React)

---

**계속 배우고 성장하세요! 🚀**

*"학습은 마라톤입니다. 천천히, 꾸준히, 즐겁게!"*

---

**작성일**: 2026-01-18
**버전**: 1.0
