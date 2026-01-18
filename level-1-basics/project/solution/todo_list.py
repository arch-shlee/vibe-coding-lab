"""
Todo List 애플리케이션

TDD로 개발한 간단한 할 일 관리 앱입니다.
"""
from typing import Dict, List


class TodoList:
    """할 일 목록을 관리하는 클래스"""

    def __init__(self):
        """TodoList 초기화"""
        self._todos: Dict[int, Dict] = {}  # id를 키로 하는 todo 딕셔너리
        self._next_id: int = 1  # 다음에 사용할 ID

    def add(self, title: str) -> Dict:
        """
        새로운 할 일을 추가합니다.

        Args:
            title: 할 일 제목

        Returns:
            생성된 todo 객체 (id, title, completed 포함)

        Raises:
            ValueError: 제목이 빈 문자열인 경우
        """
        if not title or not title.strip():
            raise ValueError("할 일 제목은 비어있을 수 없습니다")

        todo = {
            "id": self._next_id,
            "title": title.strip(),
            "completed": False
        }

        self._todos[self._next_id] = todo
        self._next_id += 1

        return todo

    def get_all(self) -> List[Dict]:
        """
        모든 할 일을 조회합니다.

        Returns:
            모든 todo의 리스트
        """
        return list(self._todos.values())

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
        if todo_id not in self._todos:
            raise KeyError(f"ID {todo_id}인 할 일을 찾을 수 없습니다")

        self._todos[todo_id]["completed"] = True
        return self._todos[todo_id]

    def delete(self, todo_id: int) -> bool:
        """
        할 일을 삭제합니다.

        Args:
            todo_id: 삭제할 todo의 ID

        Returns:
            삭제 성공 여부 (항상 True)

        Raises:
            KeyError: 해당 ID의 todo가 존재하지 않는 경우
        """
        if todo_id not in self._todos:
            raise KeyError(f"ID {todo_id}인 할 일을 찾을 수 없습니다")

        del self._todos[todo_id]
        return True

    def get_by_id(self, todo_id: int) -> Dict:
        """
        특정 ID의 할 일을 조회합니다.

        Args:
            todo_id: 조회할 todo의 ID

        Returns:
            해당 todo 객체

        Raises:
            KeyError: 해당 ID의 todo가 존재하지 않는 경우
        """
        if todo_id not in self._todos:
            raise KeyError(f"ID {todo_id}인 할 일을 찾을 수 없습니다")

        return self._todos[todo_id]

    def get_completed(self) -> List[Dict]:
        """
        완료된 할 일만 조회합니다.

        Returns:
            완료된 todo의 리스트
        """
        return [todo for todo in self._todos.values() if todo["completed"]]

    def get_incomplete(self) -> List[Dict]:
        """
        미완료된 할 일만 조회합니다.

        Returns:
            미완료된 todo의 리스트
        """
        return [todo for todo in self._todos.values() if not todo["completed"]]
