"""
 * Author: Noam527
 * Description:
"""
mod = 1_000_000_007
def modpow(b, e):
    ans = 1
    while e:
        if e & 1:
            ans = ans * b % mod
        b, e = b * b % mod, e // 2
    return ans
