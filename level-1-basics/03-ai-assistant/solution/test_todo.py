"""
TODO 앱 테스트

pytest를 사용하여 TODO 앱의 모든 기능을 테스트합니다.
"""

import pytest
from pathlib import Path
import todo


# 각 테스트 전에 TODO 목록 초기화
@pytest.fixture(autouse=True)
def reset_todos():
    """각 테스트 전에 TODO 목록을 초기화합니다."""
    todo.clear_todos()
    yield
    todo.clear_todos()


# ============================================
# add_todo() 테스트
# ============================================

def test_add_todo():
    """TODO 추가 - 정상 케이스"""
    # Given: 빈 TODO 목록
    assert len(todo.list_todos()) == 0

    # When: TODO 추가
    todo.add_todo("할 일")

    # Then: TODO가 추가됨
    assert len(todo.list_todos()) == 1
    assert todo.list_todos()[0]["title"] == "할 일"
    assert todo.list_todos()[0]["completed"] is False


def test_add_todo_with_priority():
    """TODO 추가 - 우선순위 포함"""
    # Given-When: 우선순위와 함께 TODO 추가
    todo.add_todo("긴급 업무", "high")

    # Then: 우선순위가 저장됨
    assert todo.list_todos()[0]["priority"] == "high"


def test_add_todo_default_priority():
    """TODO 추가 - 기본 우선순위"""
    # Given-When: 우선순위 없이 TODO 추가
    todo.add_todo("일반 업무")

    # Then: 기본값 medium
    assert todo.list_todos()[0]["priority"] == "medium"


def test_add_todo_empty_title():
    """TODO 추가 - 빈 제목 (에러)"""
    # Given-When-Then: 빈 제목은 ValueError 발생
    with pytest.raises(ValueError, match="비어있을 수 없습니다"):
        todo.add_todo("")


def test_add_todo_whitespace_title():
    """TODO 추가 - 공백만 있는 제목 (에러)"""
    # Given-When-Then: 공백만 있으면 ValueError
    with pytest.raises(ValueError):
        todo.add_todo("   ")


def test_add_todo_invalid_priority():
    """TODO 추가 - 잘못된 우선순위 (에러)"""
    # Given-When-Then: 잘못된 우선순위는 ValueError
    with pytest.raises(ValueError, match="우선순위는"):
        todo.add_todo("할 일", "invalid")  # type: ignore


def test_add_multiple_todos():
    """TODO 추가 - 여러 개"""
    # Given-When: 여러 TODO 추가
    todo.add_todo("할 일 1")
    todo.add_todo("할 일 2")
    todo.add_todo("할 일 3")

    # Then: 모두 추가됨
    assert len(todo.list_todos()) == 3


# ============================================
# list_todos() 테스트
# ============================================

def test_list_todos_empty():
    """TODO 목록 - 빈 목록"""
    # Given-When: 빈 TODO
    result = todo.list_todos()

    # Then: 빈 리스트 반환
    assert result == []


def test_list_todos():
    """TODO 목록 - 정상 조회"""
    # Given: TODO 추가
    todo.add_todo("할 일 1")
    todo.add_todo("할 일 2")

    # When: 목록 조회
    result = todo.list_todos()

    # Then: 모든 TODO 반환
    assert len(result) == 2
    assert result[0]["title"] == "할 일 1"
    assert result[1]["title"] == "할 일 2"


def test_list_todos_returns_copy():
    """TODO 목록 - 원본 보호"""
    # Given: TODO 추가
    todo.add_todo("할 일")

    # When: 목록 조회 후 수정
    result = todo.list_todos()
    result.append({"title": "가짜", "completed": False})

    # Then: 원본은 변경되지 않음
    assert len(todo.list_todos()) == 1


def test_list_todos_sort_by_priority():
    """TODO 목록 - 우선순위순 정렬"""
    # Given: 다양한 우선순위로 TODO 추가
    todo.add_todo("낮음", "low")
    todo.add_todo("높음", "high")
    todo.add_todo("중간", "medium")

    # When: 우선순위순 정렬
    result = todo.list_todos(sort_by_priority=True)

    # Then: high > medium > low 순서
    assert result[0]["priority"] == "high"
    assert result[1]["priority"] == "medium"
    assert result[2]["priority"] == "low"


# ============================================
# complete_todo() 테스트
# ============================================

def test_complete_todo():
    """TODO 완료 - 정상 케이스"""
    # Given: TODO 추가
    todo.add_todo("할 일")

    # When: 완료 처리
    todo.complete_todo(0)

    # Then: completed가 True
    assert todo.list_todos()[0]["completed"] is True


def test_complete_todo_invalid_index():
    """TODO 완료 - 잘못된 인덱스 (에러)"""
    # Given: TODO 1개
    todo.add_todo("할 일")

    # When-Then: 잘못된 인덱스는 IndexError
    with pytest.raises(IndexError, match="잘못된 인덱스"):
        todo.complete_todo(1)


def test_complete_todo_negative_index():
    """TODO 완료 - 음수 인덱스 (에러)"""
    # Given: TODO 1개
    todo.add_todo("할 일")

    # When-Then: 음수 인덱스는 IndexError
    with pytest.raises(IndexError):
        todo.complete_todo(-1)


def test_complete_multiple_todos():
    """TODO 완료 - 여러 개"""
    # Given: TODO 3개
    todo.add_todo("할 일 1")
    todo.add_todo("할 일 2")
    todo.add_todo("할 일 3")

    # When: 일부만 완료
    todo.complete_todo(0)
    todo.complete_todo(2)

    # Then: 해당 TODO만 완료됨
    todos = todo.list_todos()
    assert todos[0]["completed"] is True
    assert todos[1]["completed"] is False
    assert todos[2]["completed"] is True


# ============================================
# delete_todo() 테스트
# ============================================

def test_delete_todo():
    """TODO 삭제 - 정상 케이스"""
    # Given: TODO 2개
    todo.add_todo("할 일 1")
    todo.add_todo("할 일 2")

    # When: 첫 번째 삭제
    todo.delete_todo(0)

    # Then: 1개 남음
    assert len(todo.list_todos()) == 1
    assert todo.list_todos()[0]["title"] == "할 일 2"


def test_delete_todo_invalid_index():
    """TODO 삭제 - 잘못된 인덱스 (에러)"""
    # Given: TODO 1개
    todo.add_todo("할 일")

    # When-Then: 잘못된 인덱스는 IndexError
    with pytest.raises(IndexError):
        todo.delete_todo(5)


def test_delete_all_todos():
    """TODO 삭제 - 모두 삭제"""
    # Given: TODO 3개
    todo.add_todo("할 일 1")
    todo.add_todo("할 일 2")
    todo.add_todo("할 일 3")

    # When: 모두 삭제 (역순으로)
    todo.delete_todo(2)
    todo.delete_todo(1)
    todo.delete_todo(0)

    # Then: 빈 목록
    assert len(todo.list_todos()) == 0


# ============================================
# 파일 저장/로드 테스트
# ============================================

def test_save_to_file(tmp_path):
    """파일 저장 - 정상 케이스"""
    # Given: TODO 추가
    todo.add_todo("할 일 1", "high")
    todo.add_todo("할 일 2", "low")

    # When: 파일 저장
    test_file = tmp_path / "test_todos.json"
    todo.save_to_file(str(test_file))

    # Then: 파일 생성됨
    assert test_file.exists()


def test_load_from_file(tmp_path):
    """파일 로드 - 정상 케이스"""
    # Given: TODO 저장
    todo.add_todo("할 일 1", "high")
    todo.add_todo("할 일 2", "low")
    test_file = tmp_path / "test_todos.json"
    todo.save_to_file(str(test_file))

    # When: 초기화 후 로드
    todo.clear_todos()
    todo.load_from_file(str(test_file))

    # Then: 데이터 복원됨
    todos = todo.list_todos()
    assert len(todos) == 2
    assert todos[0]["title"] == "할 일 1"
    assert todos[0]["priority"] == "high"


def test_load_from_nonexistent_file(tmp_path):
    """파일 로드 - 파일이 없는 경우"""
    # Given: 존재하지 않는 파일
    test_file = tmp_path / "nonexistent.json"

    # When: 로드 시도
    todo.load_from_file(str(test_file))

    # Then: 빈 TODO로 시작
    assert len(todo.list_todos()) == 0


def test_save_and_load_preserves_state(tmp_path):
    """파일 저장/로드 - 상태 보존"""
    # Given: TODO 추가 및 완료 처리
    todo.add_todo("할 일 1", "high")
    todo.add_todo("할 일 2", "medium")
    todo.complete_todo(0)

    # When: 저장 후 로드
    test_file = tmp_path / "test_todos.json"
    todo.save_to_file(str(test_file))
    todo.clear_todos()
    todo.load_from_file(str(test_file))

    # Then: 완료 상태도 복원됨
    todos = todo.list_todos()
    assert todos[0]["completed"] is True
    assert todos[1]["completed"] is False


# ============================================
# 통합 테스트
# ============================================

def test_full_workflow():
    """전체 워크플로우 테스트"""
    # 1. TODO 추가
    todo.add_todo("긴급 업무", "high")
    todo.add_todo("일반 업무", "medium")
    todo.add_todo("나중에 할 일", "low")

    # 2. 목록 확인
    assert len(todo.list_todos()) == 3

    # 3. 우선순위순 정렬
    sorted_todos = todo.list_todos(sort_by_priority=True)
    assert sorted_todos[0]["priority"] == "high"

    # 4. 완료 처리
    todo.complete_todo(0)
    assert todo.list_todos()[0]["completed"] is True

    # 5. 삭제
    todo.delete_todo(1)
    assert len(todo.list_todos()) == 2

    # 6. 최종 확인
    remaining = todo.list_todos()
    assert remaining[0]["title"] == "긴급 업무"
    assert remaining[1]["title"] == "나중에 할 일"
