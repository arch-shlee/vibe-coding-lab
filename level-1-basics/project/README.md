# Project - Todo List 앱: Level 1 종합 프로젝트

> Level 1에서 배운 바이브코딩과 TDD를 종합하여 실전 Todo List 앱을 만들어봅니다.

## 🎯 프로젝트 목표

- Level 1에서 배운 모든 개념을 실전에 적용하기
- TDD로 완전한 기능을 가진 애플리케이션 개발
- AI와 협업하여 품질 높은 코드 작성
- 테스트 커버리지 80% 이상 달성

**예상 소요 시간**: 4-6시간

---

## 📋 프로젝트 개요

### 무엇을 만드나요?

**간단하지만 완전한 Todo List 애플리케이션**

사용자는 할 일을 추가하고, 완료 표시하고, 삭제하고, 목록을 조회할 수 있습니다.

### 왜 Todo List인가요?

✅ **적절한 복잡도**
- 너무 쉽지도, 어렵지도 않은 난이도
- 기본 CRUD 기능 포함

✅ **TDD 실습에 최적**
- 명확한 요구사항
- 테스트하기 쉬운 기능들
- 단계적 확장 가능

✅ **실용성**
- 실제로 사용할 수 있는 앱
- 추가 기능 확장 가능

---

## 🎯 요구사항

### 핵심 기능

#### 1. Todo 추가
```python
# 사용자가 할 일을 추가할 수 있어야 함
todo = TodoList()
todo.add("Python 공부하기")
todo.add("운동하기")
```

#### 2. Todo 목록 조회
```python
# 모든 할 일을 조회할 수 있어야 함
todos = todo.get_all()
# [
#   {"id": 1, "title": "Python 공부하기", "completed": False},
#   {"id": 2, "title": "운동하기", "completed": False}
# ]
```

#### 3. Todo 완료 표시
```python
# 할 일을 완료 처리할 수 있어야 함
todo.complete(1)
# {"id": 1, "title": "Python 공부하기", "completed": True}
```

#### 4. Todo 삭제
```python
# 할 일을 삭제할 수 있어야 함
todo.delete(1)
```

### 상세 요구사항

#### Todo 데이터 구조
각 Todo는 다음 속성을 가져야 합니다:
- `id`: 고유 식별자 (정수, 자동 증가)
- `title`: 할 일 제목 (문자열, 필수)
- `completed`: 완료 여부 (불린, 기본값 False)

#### 동작 규칙

**추가 (add)**:
- 빈 문자열은 추가할 수 없음
- 성공 시 생성된 Todo 객체 반환
- ID는 자동으로 1씩 증가

**조회 (get_all)**:
- 모든 Todo를 리스트로 반환
- 빈 리스트인 경우 빈 배열 반환

**완료 (complete)**:
- 존재하는 ID에 대해서만 완료 처리
- 존재하지 않는 ID는 예외 발생
- 완료된 Todo 객체 반환

**삭제 (delete)**:
- 존재하는 ID에 대해서만 삭제
- 존재하지 않는 ID는 예외 발생
- 삭제 성공 시 True 반환

---

## 🧪 테스트 요구사항

### 필수 테스트 케이스

각 기능에 대해 다음 테스트를 작성해야 합니다:

#### 1. Todo 추가 테스트
- [ ] 정상적으로 Todo를 추가할 수 있다
- [ ] 빈 문자열은 추가할 수 없다
- [ ] ID가 자동으로 증가한다
- [ ] 추가된 Todo의 completed는 False이다

#### 2. Todo 조회 테스트
- [ ] 빈 리스트를 조회할 수 있다
- [ ] 여러 Todo를 조회할 수 있다
- [ ] 조회된 Todo의 구조가 올바르다

#### 3. Todo 완료 테스트
- [ ] 정상적으로 Todo를 완료 처리할 수 있다
- [ ] 존재하지 않는 ID는 예외가 발생한다
- [ ] 완료 후 completed가 True로 변경된다

#### 4. Todo 삭제 테스트
- [ ] 정상적으로 Todo를 삭제할 수 있다
- [ ] 존재하지 않는 ID는 예외가 발생한다
- [ ] 삭제 후 목록에서 제거된다

### 테스트 커버리지
- **목표**: 80% 이상
- **측정**: pytest-cov 사용

---

## 🚀 시작하기

### 1. 환경 설정

```bash
# project/starter 폴더로 이동
cd level-1-basics/project/starter

# 가상 환경 생성 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. TDD 사이클로 개발

**Red-Green-Refactor**를 반복하며 개발하세요:

1. 🔴 **Red**: 실패하는 테스트 작성
2. 🟢 **Green**: 테스트를 통과하는 최소 코드
3. 🔵 **Refactor**: 코드 개선

### 3. AI와 협업

안티그라비티에서 Claude Sonnet 4.5와 함께 작업하세요:

**효과적인 프롬프트 예시**:
```
Todo List 앱을 TDD로 만들고 있어.
먼저 Todo 추가 기능의 테스트를 작성해줘.
- 정상 케이스
- 빈 문자열 예외 케이스
- ID 자동 증가 확인
pytest 형식으로 작성해줘.
```

---

## 📝 개발 가이드

### 추천 개발 순서

#### Phase 1: 기본 구조 (30분)
1. TodoList 클래스 뼈대 작성
2. 첫 테스트 작성 (add 기능)
3. TDD 사이클 체험

#### Phase 2: 핵심 기능 (2시간)
1. add 기능 완성
2. get_all 기능 완성
3. complete 기능 완성
4. delete 기능 완성

#### Phase 3: 예외 처리 (1시간)
1. 입력 검증
2. 에러 핸들링
3. 엣지 케이스 처리

#### Phase 4: 리팩토링 (1-2시간)
1. 코드 정리
2. 테스트 개선
3. 문서화

---

## 📚 참고 자료

### 배운 내용 복습
- [01-hello-vibe](../01-hello-vibe/): 바이브코딩 기본
- [02-first-tdd](../02-first-tdd/): TDD 사이클
- [03-ai-assistant](../03-ai-assistant/): AI 활용법

### 기술 문서
- [pytest 공식 문서](https://docs.pytest.org/)
- [Python 클래스 튜토리얼](https://docs.python.org/3/tutorial/classes.html)

### 코드 예시
- [solution/](./solution/): 막힐 때만 참고하세요!

---

## ✅ 완료 기준

### 기능 완성도
- [ ] 모든 핵심 기능 구현 완료
- [ ] 모든 테스트 통과
- [ ] 테스트 커버리지 80% 이상

### 코드 품질
- [ ] 명확한 함수/변수 이름
- [ ] 적절한 주석 (한글)
- [ ] DRY 원칙 준수
- [ ] 예외 처리 완료

### TDD 실천
- [ ] 테스트를 먼저 작성했다
- [ ] Red-Green-Refactor 사이클을 따랐다
- [ ] 커밋 메시지가 명확하다

---

## 🎓 학습 점검

프로젝트를 완료한 후 다음 질문에 답해보세요:

### 자기 평가
1. TDD의 장점을 실감했나요?
2. AI와의 협업이 효율적이었나요?
3. 어떤 부분이 가장 어려웠나요?
4. 어떤 부분에서 성장했나요?

### 개선 아이디어
- 추가하고 싶은 기능은?
- 더 나은 설계 방법은?
- 테스트를 개선할 방법은?

---

## 🎉 다음 단계

### 선택적 확장 기능

프로젝트를 완료했다면 추가 기능에 도전해보세요:

#### 레벨 ⭐
- [ ] Todo 수정 기능 (update)
- [ ] 완료된 Todo만 조회
- [ ] 미완료 Todo만 조회

#### 레벨 ⭐⭐
- [ ] Todo 우선순위 설정
- [ ] 마감일 추가
- [ ] Todo 검색 기능

#### 레벨 ⭐⭐⭐
- [ ] 파일로 저장/불러오기 (JSON)
- [ ] CLI (Command Line Interface)
- [ ] 간단한 웹 인터페이스 (Flask)

### Level 2로 진행

프로젝트를 완료하고 확장 기능까지 도전했다면:

1. [Level 2: 중급](../../level-2-intermediate/README.md)으로 진행
2. 더 복잡한 비즈니스 로직 다루기
3. 프롬프트 엔지니어링 심화

---

## 🆘 도움이 필요하신가요?

### 단계별 가이드
- [GUIDE.md](./GUIDE.md): 상세한 단계별 가이드

### 체크포인트
- [checkpoints/](./checkpoints/): 진행 상황 점검

### 커뮤니티
- [GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)
- [GitHub Issues](https://github.com/arch-shlee/vibe-coding-lab/issues)

---

## 💬 프로젝트 후기 공유

프로젝트를 완료하면 GitHub Discussions에 후기를 공유해주세요:

- 개발 과정에서의 인사이트
- TDD 실천 경험
- AI 협업 팁
- 다른 학습자를 위한 조언

---

**프로젝트**: Todo List 앱
**레벨**: Level 1 (기초)
**난이도**: ⭐⭐☆☆☆
**예상 시간**: 4-6시간
**작성일**: 2026-01-18
