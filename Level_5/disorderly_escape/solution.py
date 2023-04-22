"""This module contains the solution for the level 5 problem."""

from math import factorial as fact
from collections import Counter
from itertools import product as iproduct

def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def partitions(n, i=1):
    """Return a list of all partitions of n."""
    if n == 0:
        yield []
    for k in range(i, n+1):
        for p in partitions(n-k, k):
            yield [k] + p

def num_permutations(n, partition):
    """Return the number of permutations of the given partition."""
    r = fact(n)
    c = Counter(partition)
    p = 1
    for k, c_k in c.items():
        p *= fact(c_k) * k ** c_k
    return r // p

def log_fixed(p, q):
    """Return the number of cycles of the given configuration."""
    result = sum(gcd(i, j) for i in p for j in q)
    return int(result)

def solution(w, h, s):
    """Solves the problem."""
    RP = [tuple(p) for p in partitions(h)]
    CP = [tuple(p) for p in partitions(w)]

    RP_perms = {rp: num_permutations(h, rp) for rp in RP}
    CP_perms = (
        RP_perms if w == h else
        {cp: num_permutations(w, cp) for cp in CP}
    )

    result = sum(
        RP_perms[rp] * CP_perms[cp] * (s ** log_fixed(rp, cp))
        for rp, cp in iproduct(RP, CP)
    )

    return str(result // (fact(w) * fact(h)))
