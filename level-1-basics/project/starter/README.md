# Starter - Todo List 프로젝트 시작 템플릿

> TDD로 Todo List 앱을 만들기 위한 시작 템플릿입니다.

## 📂 파일 구조

```
starter/
├── README.md           # 이 파일
├── todo_list.py        # TodoList 클래스 구현 (여기에 코드 작성)
├── test_todo_list.py   # 테스트 작성 (여기에 테스트 작성)
└── requirements.txt    # 필요한 패키지 목록
```

---

## 🚀 시작하기

### 1. 환경 설정

```bash
# 이 폴더(starter)에서 실행

# 가상 환경 생성 (선택사항, 권장)
python -m venv venv

# 가상 환경 활성화
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 테스트 실행

```bash
# 모든 테스트 실행
pytest test_todo_list.py -v

# 특정 테스트만 실행
pytest test_todo_list.py::test_todo_list_초기화 -v

# 커버리지와 함께 실행
pytest test_todo_list.py --cov=todo_list --cov-report=term-missing
```

---

## 📖 개발 가이드

### TDD 사이클 따르기

모든 기능을 다음 순서로 개발하세요:

#### 🔴 Red (빨강)
1. `test_todo_list.py`에 테스트 작성
2. 테스트 실행 → 실패 확인 (빨간불)

#### 🟢 Green (초록)
3. `todo_list.py`에 최소한의 코드 작성
4. 테스트 실행 → 통과 확인 (초록불)

#### 🔵 Refactor (파랑)
5. 코드 개선 (가독성, 구조)
6. 테스트 실행 → 여전히 통과 확인

### AI와 협업하기

안티그라비티에서 Claude Sonnet 4.5와 함께 작업하세요:

**예시 프롬프트**:
```
test_todo_list.py에 Todo 추가 기능의 테스트를 작성해줘.

요구사항:
- 메서드: add(title)
- 반환: {"id": 1, "title": "...", "completed": False}
- 테스트 함수명: test_todo_추가

pytest 형식으로 작성해줘.
```

---

## 🎯 구현할 기능

### 1. Todo 추가 (add)
- [ ] 정상 추가 테스트
- [ ] ID 자동 증가 테스트
- [ ] 빈 문자열 예외 테스트

### 2. Todo 조회 (get_all)
- [ ] 빈 리스트 조회 테스트
- [ ] 여러 Todo 조회 테스트

### 3. Todo 완료 (complete)
- [ ] 정상 완료 테스트
- [ ] 존재하지 않는 ID 예외 테스트

### 4. Todo 삭제 (delete)
- [ ] 정상 삭제 테스트
- [ ] 존재하지 않는 ID 예외 테스트

---

## 📝 체크포인트

각 기능을 완성할 때마다 체크하세요:

- [ ] 테스트를 먼저 작성했다 (Red)
- [ ] 테스트가 실패하는 것을 확인했다
- [ ] 최소한의 코드로 테스트를 통과시켰다 (Green)
- [ ] 코드를 리팩토링했다 (Refactor)
- [ ] 리팩토링 후에도 테스트가 통과한다

---

## 🆘 도움이 필요하신가요?

### 가이드 문서
- [GUIDE.md](../GUIDE.md): 단계별 상세 가이드
- [../README.md](../README.md): 프로젝트 개요

### 막혔을 때
1. **AI에게 질문하기**
   - 에러 메시지를 보여주고 도움 요청
   - "이 기능을 어떻게 구현하나요?" 질문

2. **체크포인트 확인**
   - [../checkpoints/README.md](../checkpoints/README.md)

3. **Solution 참고** (최후의 수단)
   - [../solution/](../solution/)

---

## 💡 팁

### 테스트 작성 팁
```python
# 명확한 테스트 함수명 (한글 OK!)
def test_todo_추가():
    """무엇을 테스트하는지 설명"""
    # Given: 준비
    todo_list = TodoList()

    # When: 실행
    result = todo_list.add("할 일")

    # Then: 검증
    assert result["title"] == "할 일"
```

### AI 활용 팁
- 구체적으로 요청하기
- 한 번에 하나의 기능만
- 이해 안 되면 설명 요청
- 더 간단하게 요청 가능

---

## 🎯 목표

이 프로젝트를 완료하면:

- ✅ TDD의 Red-Green-Refactor 사이클을 체득
- ✅ pytest를 활용한 테스트 작성 능력 향상
- ✅ AI와 효과적으로 협업하는 방법 습득
- ✅ 클래스 기반 Python 프로그래밍 실습

---

**Happy Coding! 🚀**

*"테스트를 먼저 작성하면, 두려움 없이 코드를 작성할 수 있습니다." - Kent Beck*
