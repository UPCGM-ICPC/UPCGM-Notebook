"""
* Author: Gabin Dudillieu
* Date: 2024-01-26
* Description: Prime sieve for generating all primes smaller than LIM.
* Time: LIM=1e9 $\approx$ 1.5s
"""
def SieveOfEratosthenes(num):
    result = []
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            result.append(p)
    return result
