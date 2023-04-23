"""This module contains the solution for one of the Level 4 problems."""

from itertools import combinations

def solution(num_buns, num_required):
    """
    This function returns a list of key distribution such that
    any num_required bunnies can open the locks.
    """

    # Minimum number of copies required for num_required bunnies to open the locks
    number_of_key_copies = num_buns - num_required + 1

    # Get all possible bunnies combination a single key could be given to
    bunnies_combinations = combinations(range(num_buns), number_of_key_copies)

    # Assing keys in lexicographical order
    key_distribution = [[] for _ in range(num_buns)]
    for key, bunnies in enumerate(bunnies_combinations):
        for bunny in bunnies:
            key_distribution[bunny].append(key)

    return key_distribution
