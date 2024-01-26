"""
 * Author: Simon Lindholm
 * Source: kactl
 * Description: Pre-computation of modular inverses. Assumes LIM $\le$ mod and that mod is a prime.
"""
mod, LIM = 1_000_000_007, 200_000
inv = [0, 1] + [0] * (LIM - 1)
for i in range(2, LIM):
    inv[i] = mod - (mod // i) * inv[mod % i] % mod
