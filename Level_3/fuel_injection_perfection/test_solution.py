"""This module tests the solution for one of the Level 3 problems."""

from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert  solution("4") == 2
    assert solution("15") == 5
    assert solution("1") == 0
    assert solution(str(2**100 - 1)) == 101

test_solution()
