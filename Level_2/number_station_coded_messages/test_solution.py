from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution([4, 3, 10, 2, 8], 12) == [2, 3]
    assert solution([1, 2, 3, 4], 15) == [-1, -1]

test_solution()