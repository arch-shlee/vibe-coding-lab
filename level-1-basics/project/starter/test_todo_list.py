"""
Todo List 테스트

TDD의 Red-Green-Refactor 사이클을 따라 작성합니다.
"""
import pytest
from todo_list import TodoList


def test_todo_list_초기화():
    """TodoList를 생성할 수 있어야 함"""
    todo = TodoList()
    assert todo is not None


# TODO: 여기에 테스트들을 작성하세요
#
# 테스트 작성 가이드:
# 1. 테스트 함수명은 test_로 시작
# 2. 한글 함수명 사용 가능
# 3. 명확한 docstring 작성
#
# 예시:
# def test_todo_추가():
#     """Todo를 추가할 수 있어야 함"""
#     todo_list = TodoList()
#     result = todo_list.add("Python 공부")
#     assert result is not None
