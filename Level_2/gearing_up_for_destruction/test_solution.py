from solution import solution

def test_solution():
    """Test cases for solution.py"""
    assert solution([4, 30, 50]) == [12, 1]
    assert solution([4, 17, 50]) == [-1, -1]

test_solution()