from __future__ import division
import math


class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        i = -1 if (numer > 0 and denom < 0) or (numer < 0 and denom < 0) else 1
        self.numer = numer // gcd * i
        self.denom = denom // gcd * i

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + self.denom * other.numer,
            self.denom * other.denom,
        )

    def __sub__(self, other):
        return Rational(
            self.numer * other.denom - self.denom * other.numer,
            self.denom * other.denom,
        )

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return self.qthroot(base ** self.numer, self.denom)

    @staticmethod
    def qthroot(p, q):
        return p ** (1 / float(q))
