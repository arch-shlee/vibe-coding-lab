"""
계산기 테스트

TDD의 Red-Green-Refactor 사이클을 따라 작성합니다.
"""
import pytest
from calculator import calculate


def test_calculator_초기화():
    """calculate 함수가 존재하는지 확인"""
    assert calculate is not None


# TODO: 여기에 테스트를 작성하세요!
#
# TDD 가이드:
# 1. 🔴 Red: 실패하는 테스트 작성
# 2. 🟢 Green: 최소한의 코드로 통과
# 3. 🔵 Refactor: 코드 개선
#
# Phase 1: 기본 연산
# def test_두_숫자_덧셈():
#     """2 + 3 = 5"""
#     result = calculate("2 + 3")
#     assert result == 5
#
# def test_뺄셈():
#     result = calculate("10 - 4")
#     assert result == 6
#
# ... 계속 작성하세요!
