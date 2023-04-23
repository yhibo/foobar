"""This module tests the solution of one of the Level 4 problems."""

from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution(2, 1) == [[0], [0]]
    assert solution(4, 4) == [[0], [1], [2], [3]]
    assert solution(5, 3) == [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9],
                              [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]

test_solution()
