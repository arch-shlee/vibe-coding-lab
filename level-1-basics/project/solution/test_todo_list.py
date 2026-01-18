"""
Todo List 테스트

TDD의 Red-Green-Refactor 사이클을 따라 작성한 완전한 테스트 스위트입니다.
"""
import pytest
from todo_list import TodoList


# ========== 초기화 테스트 ==========

def test_todo_list_초기화():
    """TodoList를 생성할 수 있어야 함"""
    todo_list = TodoList()
    assert todo_list is not None


# ========== Todo 추가 테스트 ==========

def test_todo_추가():
    """Todo를 추가할 수 있어야 함"""
    todo_list = TodoList()
    result = todo_list.add("Python 공부하기")

    assert result is not None
    assert result["id"] == 1
    assert result["title"] == "Python 공부하기"
    assert result["completed"] == False


def test_여러_todo_추가():
    """여러 개의 Todo를 추가하면 ID가 증가해야 함"""
    todo_list = TodoList()

    todo1 = todo_list.add("첫 번째 할 일")
    todo2 = todo_list.add("두 번째 할 일")
    todo3 = todo_list.add("세 번째 할 일")

    assert todo1["id"] == 1
    assert todo2["id"] == 2
    assert todo3["id"] == 3


def test_빈_문자열_추가_실패():
    """빈 문자열은 추가할 수 없어야 함"""
    todo_list = TodoList()

    with pytest.raises(ValueError, match="비어있을 수 없습니다"):
        todo_list.add("")


def test_공백만_있는_문자열_추가_실패():
    """공백만 있는 문자열은 추가할 수 없어야 함"""
    todo_list = TodoList()

    with pytest.raises(ValueError):
        todo_list.add("   ")


def test_앞뒤_공백_제거():
    """Todo 제목의 앞뒤 공백이 제거되어야 함"""
    todo_list = TodoList()
    result = todo_list.add("  Python 공부  ")

    assert result["title"] == "Python 공부"


# ========== Todo 조회 테스트 ==========

def test_빈_리스트_조회():
    """빈 TodoList를 조회하면 빈 리스트를 반환해야 함"""
    todo_list = TodoList()
    todos = todo_list.get_all()

    assert todos == []
    assert len(todos) == 0


def test_여러_todo_조회():
    """여러 Todo를 추가한 후 조회할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("첫 번째")
    todo_list.add("두 번째")
    todo_list.add("세 번째")

    todos = todo_list.get_all()

    assert len(todos) == 3
    assert todos[0]["title"] == "첫 번째"
    assert todos[1]["title"] == "두 번째"
    assert todos[2]["title"] == "세 번째"


def test_조회된_todo_구조():
    """조회된 Todo가 올바른 구조를 가져야 함"""
    todo_list = TodoList()
    todo_list.add("테스트 할 일")

    todos = todo_list.get_all()
    todo = todos[0]

    assert "id" in todo
    assert "title" in todo
    assert "completed" in todo
    assert isinstance(todo["id"], int)
    assert isinstance(todo["title"], str)
    assert isinstance(todo["completed"], bool)


# ========== Todo 완료 테스트 ==========

def test_todo_완료():
    """Todo를 완료 처리할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("운동하기")

    result = todo_list.complete(1)

    assert result["id"] == 1
    assert result["completed"] == True


def test_여러_todo_중_하나만_완료():
    """여러 Todo 중 특정 Todo만 완료 처리할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("첫 번째")
    todo_list.add("두 번째")
    todo_list.add("세 번째")

    todo_list.complete(2)

    todos = todo_list.get_all()
    assert todos[0]["completed"] == False
    assert todos[1]["completed"] == True
    assert todos[2]["completed"] == False


def test_존재하지_않는_todo_완료_실패():
    """존재하지 않는 ID는 완료 처리할 수 없어야 함"""
    todo_list = TodoList()

    with pytest.raises(KeyError, match="찾을 수 없습니다"):
        todo_list.complete(999)


def test_완료된_todo_다시_완료():
    """이미 완료된 Todo를 다시 완료 처리해도 문제없어야 함"""
    todo_list = TodoList()
    todo_list.add("할 일")
    todo_list.complete(1)

    # 다시 완료 처리
    result = todo_list.complete(1)

    assert result["completed"] == True


# ========== Todo 삭제 테스트 ==========

def test_todo_삭제():
    """Todo를 삭제할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("삭제할 할 일")

    result = todo_list.delete(1)

    assert result == True
    assert len(todo_list.get_all()) == 0


def test_여러_todo_중_하나만_삭제():
    """여러 Todo 중 특정 Todo만 삭제할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("첫 번째")
    todo_list.add("두 번째")
    todo_list.add("세 번째")

    todo_list.delete(2)

    todos = todo_list.get_all()
    assert len(todos) == 2
    assert todos[0]["title"] == "첫 번째"
    assert todos[1]["title"] == "세 번째"


def test_존재하지_않는_todo_삭제_실패():
    """존재하지 않는 ID는 삭제할 수 없어야 함"""
    todo_list = TodoList()

    with pytest.raises(KeyError, match="찾을 수 없습니다"):
        todo_list.delete(999)


def test_삭제_후_같은_id_삭제_실패():
    """삭제한 Todo를 다시 삭제하면 실패해야 함"""
    todo_list = TodoList()
    todo_list.add("할 일")
    todo_list.delete(1)

    with pytest.raises(KeyError):
        todo_list.delete(1)


# ========== 통합 시나리오 테스트 ==========

def test_전체_시나리오():
    """실제 사용 시나리오를 테스트"""
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
    assert todos[1]["title"] == "저녁 독서"
    assert todos[1]["completed"] == False


def test_복잡한_시나리오():
    """더 복잡한 사용 시나리오"""
    todo_list = TodoList()

    # 5개 추가
    for i in range(1, 6):
        todo_list.add(f"{i}번째 할 일")

    # 2개 완료
    todo_list.complete(1)
    todo_list.complete(3)

    # 1개 삭제
    todo_list.delete(2)

    # 검증
    todos = todo_list.get_all()
    assert len(todos) == 4

    # 완료된 것들 확인
    completed_todos = [t for t in todos if t["completed"]]
    assert len(completed_todos) == 2


# ========== 추가 기능 테스트 (보너스) ==========

def test_id로_조회():
    """특정 ID의 Todo를 조회할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("첫 번째")
    todo_list.add("두 번째")

    todo = todo_list.get_by_id(2)

    assert todo["id"] == 2
    assert todo["title"] == "두 번째"


def test_완료된_todo만_조회():
    """완료된 Todo만 필터링해서 조회할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("첫 번째")
    todo_list.add("두 번째")
    todo_list.add("세 번째")

    todo_list.complete(1)
    todo_list.complete(3)

    completed = todo_list.get_completed()

    assert len(completed) == 2
    assert all(t["completed"] for t in completed)


def test_미완료_todo만_조회():
    """미완료된 Todo만 필터링해서 조회할 수 있어야 함"""
    todo_list = TodoList()
    todo_list.add("첫 번째")
    todo_list.add("두 번째")
    todo_list.add("세 번째")

    todo_list.complete(2)

    incomplete = todo_list.get_incomplete()

    assert len(incomplete) == 2
    assert all(not t["completed"] for t in incomplete)
