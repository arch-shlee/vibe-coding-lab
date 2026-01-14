"""
TODO 앱 - 완전한 버전

기본 기능 + 우선순위 + 파일 저장/로드 기능을 포함한 TODO 앱입니다.
"""

import json
from pathlib import Path
from typing import Literal

# TODO 데이터 저장소
todos = []

# 우선순위 타입 (타입 힌트용)
Priority = Literal["high", "medium", "low"]

# 기본 저장 파일 경로
DEFAULT_FILE = "todos.json"


def add_todo(title: str, priority: Priority = "medium") -> None:
    """
    새로운 TODO를 추가합니다.

    Args:
        title: TODO 제목
        priority: 우선순위 (high, medium, low)

    Raises:
        ValueError: 제목이 비어있거나 우선순위가 잘못된 경우

    Examples:
        >>> add_todo("Python 공부하기", "high")
        >>> add_todo("운동하기")  # 기본값 medium
    """
    if not title or not title.strip():
        raise ValueError("제목은 비어있을 수 없습니다")

    valid_priorities = ["high", "medium", "low"]
    if priority not in valid_priorities:
        raise ValueError(f"우선순위는 {valid_priorities} 중 하나여야 합니다")

    todos.append({
        "title": title.strip(),
        "completed": False,
        "priority": priority
    })


def list_todos(sort_by_priority: bool = False) -> list:
    """
    모든 TODO 항목을 반환합니다.

    Args:
        sort_by_priority: True면 우선순위순으로 정렬

    Returns:
        TODO 목록 (딕셔너리 리스트)

    Examples:
        >>> todos = list_todos()
        >>> todos_sorted = list_todos(sort_by_priority=True)
    """
    result = todos.copy()

    if sort_by_priority:
        # 우선순위 순서: high(0) > medium(1) > low(2)
        priority_order = {"high": 0, "medium": 1, "low": 2}
        result.sort(key=lambda x: priority_order[x["priority"]])

    return result


def complete_todo(index: int) -> None:
    """
    TODO를 완료 상태로 변경합니다.

    Args:
        index: TODO 인덱스 (0부터 시작)

    Raises:
        IndexError: 잘못된 인덱스일 경우

    Examples:
        >>> add_todo("할 일")
        >>> complete_todo(0)
        >>> list_todos()[0]["completed"]
        True
    """
    if index < 0 or index >= len(todos):
        raise IndexError(f"잘못된 인덱스입니다: {index}")

    todos[index]["completed"] = True


def delete_todo(index: int) -> None:
    """
    TODO를 삭제합니다.

    Args:
        index: TODO 인덱스 (0부터 시작)

    Raises:
        IndexError: 잘못된 인덱스일 경우

    Examples:
        >>> add_todo("삭제할 항목")
        >>> delete_todo(0)
        >>> len(list_todos())
        0
    """
    if index < 0 or index >= len(todos):
        raise IndexError(f"잘못된 인덱스입니다: {index}")

    todos.pop(index)


def save_to_file(filename: str = DEFAULT_FILE) -> None:
    """
    TODO 데이터를 JSON 파일로 저장합니다.

    Args:
        filename: 저장할 파일 경로

    Raises:
        IOError: 파일 저장 실패 시

    Examples:
        >>> add_todo("할 일")
        >>> save_to_file("my_todos.json")
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise IOError(f"파일 저장 실패: {e}")


def load_from_file(filename: str = DEFAULT_FILE) -> None:
    """
    JSON 파일에서 TODO 데이터를 로드합니다.

    Args:
        filename: 로드할 파일 경로

    Raises:
        IOError: 파일 로드 실패 시

    Examples:
        >>> load_from_file("my_todos.json")
        >>> todos = list_todos()
    """
    global todos

    # 파일이 없으면 빈 TODO로 시작
    if not Path(filename).exists():
        todos = []
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            todos = json.load(f)
    except Exception as e:
        raise IOError(f"파일 로드 실패: {e}")


def clear_todos() -> None:
    """
    모든 TODO를 삭제합니다.

    테스트에서 사용하기 위한 유틸리티 함수입니다.
    """
    todos.clear()


# 데모 및 테스트용 코드
if __name__ == "__main__":
    print("=== TODO 앱 데모 (완전한 버전) ===\n")

    # 1. 기본 기능
    print("1. TODO 추가 (우선순위 포함)")
    add_todo("긴급 버그 수정", "high")
    add_todo("코드 리뷰", "medium")
    add_todo("문서 업데이트", "low")
    add_todo("회의 준비", "high")
    print(f"추가됨: {len(list_todos())}개\n")

    # 2. 일반 목록
    print("2. TODO 목록 (추가 순서)")
    for i, todo in enumerate(list_todos()):
        status = "✓" if todo["completed"] else " "
        priority = todo["priority"]
        print(f"[{status}] {i}: [{priority:6}] {todo['title']}")
    print()

    # 3. 우선순위순 정렬
    print("3. TODO 목록 (우선순위순)")
    for i, todo in enumerate(list_todos(sort_by_priority=True)):
        status = "✓" if todo["completed"] else " "
        priority = todo["priority"]
        print(f"[{status}] {i}: [{priority:6}] {todo['title']}")
    print()

    # 4. 완료 처리
    print("4. TODO 완료 처리 (인덱스 0)")
    complete_todo(0)
    for i, todo in enumerate(list_todos()):
        status = "✓" if todo["completed"] else " "
        priority = todo["priority"]
        print(f"[{status}] {i}: [{priority:6}] {todo['title']}")
    print()

    # 5. 파일 저장
    print("5. 파일로 저장")
    save_to_file("demo_todos.json")
    print("✓ 'demo_todos.json'에 저장됨\n")

    # 6. 데이터 초기화 후 로드
    print("6. 파일에서 로드")
    clear_todos()
    print(f"초기화 후: {len(list_todos())}개")
    load_from_file("demo_todos.json")
    print(f"로드 후: {len(list_todos())}개")
    for i, todo in enumerate(list_todos()):
        status = "✓" if todo["completed"] else " "
        priority = todo["priority"]
        print(f"[{status}] {i}: [{priority:6}] {todo['title']}")
    print()

    # 7. 에러 처리
    print("7. 에러 처리 테스트")
    try:
        add_todo("")
    except ValueError as e:
        print(f"✓ 빈 제목 검증: {e}")

    try:
        add_todo("할 일", "invalid")  # type: ignore
    except ValueError as e:
        print(f"✓ 우선순위 검증: {e}")

    try:
        delete_todo(999)
    except IndexError as e:
        print(f"✓ 인덱스 검증: {e}")

    # 정리
    Path("demo_todos.json").unlink(missing_ok=True)
    print("\n✓ 데모 완료")
