"""
 * Author: Lukas Polacek
 * Description: Operators for modular arithmetic.
 * For +, -, *, /, the struct will take of the left operand.
"""
from Euclid import extended_euclid_gcd
class Mod:
    def __init__(self, xx, mod):
        self.x = xx
        self.mod = mod
    def __add__(self, b):
        return Mod((self.x + b.x) % self.mod, self.mod)
    def __sub__(self, b):
        return Mod((self.x - b.x + self.mod) % self.mod, self.mod)
    def __mul__(self, b):
        return Mod((self.x * b.x) % self.mod, self.mod)
    def __truediv__(self, b):
        return self * self.invert(b)
    def invert(self, a):
        x, y, g = extended_euclid_gcd(a.x, self.mod)
        assert (g == 1)
        return Mod((x + self.mod) % self.mod, self.mod)
    def __pow__(self, e):
        if not e:
            return Mod(1, self.mod)
        r = self ** (e // 2)
        r = r * r
        return self * r if e & 1 else r
