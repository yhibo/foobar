"""This module tests the solution for one of the Level 3 problems."""

from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution([[0, 1, 1, 0],
                     [0, 0, 0, 1],
                     [1, 1, 0, 0],
                     [1, 1, 1, 0]]) == 7
    assert solution([[0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 1, 1],
                     [0, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0]]) == 11

test_solution()
