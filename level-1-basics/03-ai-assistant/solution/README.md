# 03-ai-assistant 모범 답안

> 이 폴더는 과제의 모범 답안을 포함합니다.

## ⚠️ 주의사항

**먼저 스스로 시도해보세요!**

모범 답안은 막혔을 때만 참고하세요:
- 완전히 막혔을 때
- 자신의 코드와 비교하고 싶을 때
- 다른 접근 방법을 보고 싶을 때

## 📁 파일 설명

### prompt_practice_solution.md
- 프롬프트 개선 연습의 모범 답안
- 좋은 프롬프트의 예시 포함

### todo.py
- 완전히 구현된 TODO 앱
- 기본 기능 + 우선순위 + 파일 저장

### test_todo.py
- 모든 함수에 대한 테스트
- Edge case 테스트 포함

### todo_basic.py
- 기본 기능만 구현된 버전
- 우선순위, 파일 저장 제외

## 🎯 학습 방법

### 1단계: 비교
- 자신의 코드와 모범 답안 비교
- 차이점 찾기

### 2단계: 분석
- 왜 이렇게 구현했는지 이해
- 더 나은 방법이 있는지 고민

### 3단계: 적용
- 배운 점을 자신의 코드에 적용
- 개선해보기

## 💡 주요 학습 포인트

### 1. 코드 구조
```python
# 명확한 데이터 구조
todos = []

# 함수는 한 가지 일만
def add_todo(title: str) -> None:
    """명확한 docstring"""
    # 검증
    if not title:
        raise ValueError("제목은 비어있을 수 없습니다")

    # 메인 로직
    todos.append({"title": title, "completed": False})
```

### 2. 에러 처리
```python
def delete_todo(index: int) -> None:
    """인덱스 검증"""
    if index < 0 or index >= len(todos):
        raise IndexError("잘못된 인덱스입니다")

    todos.pop(index)
```

### 3. 테스트 작성
```python
def test_add_todo():
    """Given-When-Then 패턴"""
    # Given: 초기 상태
    clear_todos()

    # When: 액션
    add_todo("할 일")

    # Then: 검증
    assert len(list_todos()) == 1
```

## 🔍 코드 리뷰 체크리스트

자신의 코드가 다음을 만족하는지 확인하세요:

### 기본 요구사항
- [ ] 모든 함수가 작동함
- [ ] 테스트가 모두 통과함
- [ ] 에러 처리가 되어 있음

### 코드 품질
- [ ] 함수명이 명확함
- [ ] 변수명이 의미있음
- [ ] 주석/docstring이 있음
- [ ] 중복 코드가 없음

### 테스트
- [ ] 정상 케이스 테스트
- [ ] Edge case 테스트
- [ ] 에러 케이스 테스트

## 🎓 더 나아가기

모범 답안을 이해했다면:

### 추가 도전 과제
1. **TODO 편집 기능**
   - 기존 TODO의 제목 수정하기

2. **마감일 추가**
   - 각 TODO에 due_date 추가
   - 마감일 지난 TODO 표시

3. **카테고리 분류**
   - TODO를 카테고리별로 분류
   - 카테고리별 조회 기능

4. **CLI 인터페이스**
   - 명령줄에서 사용 가능한 인터페이스
   - argparse 사용

---

**질문이 있나요?**
[GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)에서 물어보세요!
