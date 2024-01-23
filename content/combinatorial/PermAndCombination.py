"""
 * Author: Unknown
 * Source: https://www.geeksforgeeks.org/permutation-and-combination-in-python
 * Description: Lists permutations and combinations of a certain size from a list
 * Time: O(n!/(n-r)!) for permutations
         O(n^r)  for permutations with repetitions
         O(n!/(r!*((n-r))!)) for combinations
"""
from itertools import permutations, product, combinations
def generate_permutations(lst, r=None):
    return list(permutations(lst, r))
def generate_permutations_with_repetition(lst, r=None):
    if r == None:
        r = len(lst)
    return list(product(lst, repeat=r))
def generate_int_permutation(n, r=None):
    lst = [(j + 1) for j in range(n)]
    return list(generate_permutations(lst, r))
def generate_combination(lst, r=None):
    if r == None:
        r = len(lst)
    return list(combinations(lst, r))
