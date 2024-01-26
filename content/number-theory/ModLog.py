"""
 * Author: Bjorn Martinsson
 * Source: kactl
 * Description: Returns the smallest $x > 0$ s.t. $a^x = b \pmod m$, or
 * $-1$ if no such $x$ exists. modLog(a,1,m) can be used to
 * calculate the order of $a$.
 * Time: $O(\sqrt m)$
 * Status: tested for all 0 <= a,x < 500 and 0 < m < 500.
 *
 * Details: This algorithm uses the baby-step giant-step method to
 * find (i,j) such that a^(n * i) = b * a^j (mod m), where n > sqrt(m)
 * and 0 < i, j <= n. If a and m are coprime then a^j has a modular
 * inverse, which means that a^(i * n - j) = b (mod m$).
 *
 * However this particular implementation of baby-step giant-step works even
 * without assuming a and m are coprime, using the following idea:
 *
 * Assume p^x is a prime divisor of m. Then we have 3 cases
 *	 1. b is divisible by p^x
 *	 2. b is divisible only by some p^y, 0<y<x
 *	 3. b is not divisible by p
 * The important thing to note is that in case 2, modLog(a,b,m) (if
 * it exists) cannot be > sqrt(m), (technically it cannot be >= log2(m)).
 * So once all exponenents of a that are <= sqrt(m) has been checked, you
 * cannot have case 2. Case 2 is the only tricky case.
 *
 * So the modification allowing for non-coprime input involves checking all
 * exponents of a that are <= n, and then handling the non-tricky cases by
 * a simple gcd(a^n,m) == gcd(b,m) check.
"""
import math
def modlog(a, b, m):
    n, e, f, j = math.sqrt(m) + 1, 1, 1, 1
    d = dict()
    while (j <= n and e != b % m):
        e = e * a % m
        f = e
        d[e * b % m] = j
        j += 1
    if e == b % m:
        return j
    if math.gcd(m, e) == math.gcd(m, b):
        for i in range(2, n+2):
            e = e * f % m
            if len(filter(lambda k: k == e), d.keys()):
                return n * i - d[e]
    return -1
