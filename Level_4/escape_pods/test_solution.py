"""This module tests the solution of one of the Level 4 problems."""

from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution([0, 1], [4, 5], 
                    [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4],
                     [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 16
    assert solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == 6

test_solution()
