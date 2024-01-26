"""
* Author: Gabin Dudillieu
* Date: 2024-01-26
* Source: https://www.rookieslab.com/posts/extended-euclid-algorithm-to-find-gcd-bezouts-coefficients-python-cpp-code
* Description: Finds gcd, and finds two integers $x$ and $y$, such that $ax+by=\gcd(a,b)$. If
* you just need gcd, use the built in \texttt{\_\_gcd} instead.
* If $a$ and $b$ are coprime, then $x$ is the inverse of $a \pmod{b}$.
* Time: O(log(min(a, b)))
"""
from math import gcd
def get_gcd(a, b):
    return gcd(a, b)
def extended_euclid_gcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        quotient = old_r // r 
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]
