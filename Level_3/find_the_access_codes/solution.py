"""This module contains the solution for one of the Level 3 problems."""

def solution(l):
    """Return the number of triples in the list l."""
    n = len(l)
    divisors = [0] * n
    triples = 0

    for i in range(n):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                divisors[j] += 1
                triples += divisors[i]

    return triples
