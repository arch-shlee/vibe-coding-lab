"""
TODO 앱 - 기본 버전

기본 기능만 구현된 TODO 앱입니다.
- TODO 추가, 조회, 완료, 삭제
"""

# TODO 데이터 저장소
todos = []


def add_todo(title: str) -> None:
    """
    새로운 TODO를 추가합니다.

    Args:
        title: TODO 제목

    Raises:
        ValueError: 제목이 비어있을 경우

    Examples:
        >>> add_todo("Python 공부하기")
        >>> add_todo("운동하기")
    """
    if not title or not title.strip():
        raise ValueError("제목은 비어있을 수 없습니다")

    todos.append({
        "title": title.strip(),
        "completed": False
    })


def list_todos() -> list:
    """
    모든 TODO 항목을 반환합니다.

    Returns:
        TODO 목록 (딕셔너리 리스트)

    Examples:
        >>> todos = list_todos()
        >>> for i, todo in enumerate(todos):
        ...     print(f"{i}: {todo['title']}")
    """
    return todos.copy()  # 원본 보호를 위해 복사본 반환


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


def clear_todos() -> None:
    """
    모든 TODO를 삭제합니다.

    테스트에서 사용하기 위한 유틸리티 함수입니다.

    Examples:
        >>> add_todo("항목 1")
        >>> add_todo("항목 2")
        >>> clear_todos()
        >>> len(list_todos())
        0
    """
    todos.clear()


# 테스트 및 데모용 코드
if __name__ == "__main__":
    print("=== TODO 앱 데모 ===\n")

    # TODO 추가
    print("1. TODO 추가하기")
    add_todo("Python 공부하기")
    add_todo("운동하기")
    add_todo("책 읽기")
    print(f"추가됨: {len(list_todos())}개\n")

    # TODO 목록 보기
    print("2. TODO 목록")
    for i, todo in enumerate(list_todos()):
        status = "✓" if todo["completed"] else " "
        print(f"[{status}] {i}: {todo['title']}")
    print()

    # TODO 완료 처리
    print("3. TODO 완료 처리 (인덱스 0)")
    complete_todo(0)
    for i, todo in enumerate(list_todos()):
        status = "✓" if todo["completed"] else " "
        print(f"[{status}] {i}: {todo['title']}")
    print()

    # TODO 삭제
    print("4. TODO 삭제 (인덱스 1)")
    delete_todo(1)
    for i, todo in enumerate(list_todos()):
        status = "✓" if todo["completed"] else " "
        print(f"[{status}] {i}: {todo['title']}")
    print()

    # 에러 처리 예시
    print("5. 에러 처리 테스트")
    try:
        add_todo("")
    except ValueError as e:
        print(f"✓ 빈 제목 검증: {e}")

    try:
        delete_todo(999)
    except IndexError as e:
        print(f"✓ 인덱스 검증: {e}")
