"""This module tests the solution for one of the Level 3 problems."""

from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution([1, 1, 1]) == 1
    assert solution([1, 2, 3, 4, 5, 6]) == 3

test_solution()
