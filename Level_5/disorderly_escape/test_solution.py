"""This module tests the solution for one of the Level 3 problems."""

from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution(2, 2, 2) == str(7)
    assert solution(2, 3, 4) == str(430)
    assert solution(3, 2, 4) == str(430)
    assert solution(3, 3, 2) == str(36)
    assert solution(4, 4, 2) == str(317)
    assert solution(5, 5, 2) == str(5624)
    assert solution(6, 6, 2) == str(251610)
    assert solution(6, 4, 2) == str(3250)

test_solution()
