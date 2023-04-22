"""This module contains the solution for one of the Level 3 problems."""

def solution(n):
    """
    This function takes in an integer n and returns the minimum number of steps
    required to reach 1 using the following rules:
    - If n is even, divide it by 2.
    - If n is odd and can be expressed in the form n = 2^k + 1, subtract 1.
    - If n is odd and cannot be expressed in the form n = 2^k + 1, add 1.
    
    Parameters:
    n (int): The number to be reduced to 1.
    
    Returns:
    int: The minimum number of steps required to reach 1.
    """
    n = int(n)
    steps = 0
    while n != 1:
        if n & 1 == 0:
            n >>= 1
        elif n & 3 == 1 or n == 3:
            n -= 1
        else:
            n += 1
        steps += 1
    return steps
