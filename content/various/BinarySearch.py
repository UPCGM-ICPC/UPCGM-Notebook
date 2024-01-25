"""
 * Author: Oleksandr Kulkov
 * Source: https://cp-algorithms.com/num_methods/binary_search.html
 * Description: Binary Search among a sorted array.
 * Time: O(log n)
"""
def binarySearch(array, k):
    left, right = [0, len(array)]
    while (right - left > 0):
        m = (left + right) // 2
        if (k == array[m]):
            return True
        if (k < array[m]):
            right = m
        else:
            left = m + 1
    return k == array[m]
