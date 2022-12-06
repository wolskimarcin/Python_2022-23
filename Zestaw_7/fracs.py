from math import gcd


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if type(y) != int:
            raise TypeError("The numerator must be integer.")
        if type(x) != int:
            raise TypeError("The denominator must be integer.")
        if y == 0:
            raise ValueError("The denominator cannot be zero.")
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(str(self.x))
        else:
            return str(str(self.x) + '/' + str(self.y))

    def __repr__(self):  # zwraca "Frac(x, y)"
        return str('Frac(' + str(self.x) + ', ' + str(self.y) + ')')

    # Py2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        n1, n2 = self.x * other.y, other.x * self.y
        return n1 == n2

    def __ne__(self, other):
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        n1, n2 = self.x * other.y, other.x * self.y
        return n1 != n2

    def __lt__(self, other):
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        n1, n2 = self.x * other.y, other.x * self.y
        return n1 < n2

    def __le__(self, other):
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        n1, n2 = self.x * other.y, other.x * self.y
        return not n1 > n2

    def __gt__(self, other):
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        n1, n2 = self.x * other.y, other.x * self.y
        return n1 > n2

    def __ge__(self, other):
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        n1, n2 = self.x * other.y, other.x * self.y
        return not n1 < n2

    def __add__(self, other):  # frac1+frac2, frac+int
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        d = self.y * other.y
        n = self.x * other.y + other.x * self.y

        nwd = gcd(n, d)
        n_reduced = int(n / nwd)
        d_reduced = int(d / nwd)
        if d_reduced < 0:
            d_reduced = abs(d_reduced)
            n_reduced = 0 - n_reduced
        return Frac(n_reduced, d_reduced)

    __radd__ = __add__  # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        d = self.y * other.y
        n = self.x * other.y - other.x * self.y

        nwd = gcd(n, d)
        n_reduced = int(n / nwd)
        d_reduced = int(d / nwd)
        if d_reduced < 0:
            d_reduced = abs(d_reduced)
            n_reduced = 0 - n_reduced
        return Frac(n_reduced, d_reduced)

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])
        n = self.x * other.x
        d = self.y * other.y
        nwd = gcd(n, d)
        n = int(n / nwd)
        d = int(d / nwd)
        if d < 0:
            d = abs(d)
            n = 0 - n
        return Frac(n, d)

    __rmul__ = __mul__  # int*frac

    def __div__(self, other):   # frac1/frac2, frac/int, Py2
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        other.x, other.y = other.y, other.x
        n = self.x * other.x
        d = self.y * other.y
        nwd = gcd(n, d)
        n = int(n / nwd)
        d = int(d / nwd)
        if d < 0:
            d = abs(d)
            n = 0 - n
        return Frac(n, d)

    def __rdiv__(self, other):  # int/frac, Py2
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        other.x, other.y = other.y, other.x
        n = self.x * other.x
        d = self.y * other.y
        nwd = gcd(n, d)
        n = int(n / nwd)
        d = int(d / nwd)
        if d < 0:
            d = abs(d)
            n = 0 - n
        return Frac(n, d)

    def __truediv__(self, other):  # frac1/frac2, frac/int, Py3
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        other.x, other.y = other.y, other.x
        n = self.x * other.x
        d = self.y * other.y
        nwd = gcd(n, d)
        n = int(n / nwd)
        d = int(d / nwd)
        if d < 0:
            d = abs(d)
            n = 0 - n
        return Frac(n, d)

    def __rtruediv__(self, other):  # int/frac, Py3
        if type(other) == int:
            other = Frac(other)
        elif type(other) == float:
            int_ratio = other.as_integer_ratio()
            other = Frac(int_ratio[0], int_ratio[1])

        other.x, other.y = other.y, other.x
        n = self.x * other.x
        d = self.y * other.y
        nwd = gcd(n, d)
        n = int(n / nwd)
        d = int(d / nwd)
        if d < 0:
            d = abs(d)
            n = 0 - n
        return Frac(n, d)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return (+1) * self

    def __neg__(self):  # -frac = (-1)*frac
        return (-1) * self

    def __invert__(self):  # odwrotnosc: ~frac
        if self.x == 0:
            return self
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return float(self.x / self.y)

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])


# Kod testujący moduł.

import unittest


class TestFrac(unittest.TestCase):
    def test_init(self):
        y = 0
        self.assertRaises(ValueError, Frac, 1, y)
        self.assertRaises(TypeError, Frac, (1, 2), 'xyz')

    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), '1/2')
        self.assertEqual(str(Frac(0, 1)), '0')
        self.assertEqual(str(Frac(4, 4)), '4/4')
        self.assertEqual(str(Frac(4)), '4')

    def test_repr(self):
        self.assertEqual(repr(Frac(1, 2)), 'Frac(1, 2)')
        self.assertEqual(repr(Frac(0, 1)), 'Frac(0, 1)')
        self.assertEqual(repr(Frac(4, 4)), 'Frac(4, 4)')

    def test_eq(self):
        self.assertEqual(Frac(1, 2) == Frac(1, 2), True)
        self.assertEqual(Frac(0, 1) == Frac(0, 1), True)
        self.assertEqual(Frac(4, 1) == Frac(4), True)
        self.assertEqual(Frac(4) == 4, True)
        self.assertEqual(5 == Frac(5, 1), True)
        self.assertEqual(Frac(1, 4) == 0.25, True)
        self.assertEqual(Frac(1, 2) == 0.25, False)
        self.assertEqual(Frac(0, 1) == Frac(0, 2), True)
        self.assertEqual(Frac(4, 4) == Frac(4, 1), False)

    def test_ne(self):
        self.assertEqual(Frac(1, 2) != Frac(1, 2), False)
        self.assertEqual(Frac(0, 1) != Frac(0, 1), False)
        self.assertEqual(Frac(4, 4) != Frac(4, 4), False)
        self.assertEqual(Frac(4) != 4, False)
        self.assertEqual(5 != Frac(5, 1), False)
        self.assertEqual(Frac(1, 4) != 0.25, False)
        self.assertEqual(Frac(1, 2) != 0.25, True)
        self.assertEqual(Frac(1, 2) != Frac(2, 3), True)
        self.assertEqual(Frac(0, 1) != Frac(0, 2), False)
        self.assertEqual(Frac(4, 4) != Frac(4, 1), True)

    def test_lt(self):
        self.assertEqual(Frac(1, 2) < Frac(1, 2), False)
        self.assertEqual(Frac(0, 1) < Frac(0, 1), False)
        self.assertEqual(Frac(4) < 51331, True)
        self.assertEqual(Frac(4) < 3, False)
        self.assertEqual(Frac(1, 6) < 0.25, True)
        self.assertEqual(Frac(1, 1) < 0.25, False)
        self.assertEqual(Frac(4, 4) < Frac(4), True)
        self.assertEqual(Frac(1, 2) < Frac(3, 3), True)

    def test_le(self):
        self.assertEqual(Frac(1, 2) <= Frac(1, 2), True)
        self.assertEqual(Frac(0, 1) <= Frac(0, 1), True)
        self.assertEqual(Frac(4) <= 51331, True)
        self.assertEqual(Frac(4) <= 3, False)
        self.assertEqual(Frac(1, 6) <= 0.25, True)
        self.assertEqual(Frac(1, 4) <= 0.25, True)
        self.assertEqual(Frac(4, 4) <= Frac(4, 2), True)
        self.assertEqual(Frac(3, 2) <= Frac(3, 3), False)

    def test_gt(self):
        self.assertEqual(Frac(1, 2) > Frac(1, 2), False)
        self.assertEqual(Frac(0, 1) > Frac(0, 1), False)
        self.assertEqual(Frac(4) > 51331, False)
        self.assertEqual(Frac(4) > 3, True)
        self.assertEqual(Frac(1, 6) > 0.25, False)
        self.assertEqual(Frac(1, 1) > 0.25, True)
        self.assertEqual(Frac(4, 4) > Frac(4), False)
        self.assertEqual(Frac(1, 2) > Frac(3, 3), False)

    def test_ge(self):
        self.assertEqual(Frac(1, 2) >= Frac(1, 2), True)
        self.assertEqual(Frac(0, 1) >= Frac(0, 1), True)
        self.assertEqual(Frac(4) >= 51331, False)
        self.assertEqual(Frac(4) >= 3, True)
        self.assertEqual(Frac(1, 6) >= 0.25, False)
        self.assertEqual(Frac(1, 4) >= 0.25, True)
        self.assertEqual(Frac(4, 4) >= Frac(4, 2), False)
        self.assertEqual(Frac(3, 2) >= Frac(3, 3), True)

    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(-1, 2) + Frac(1, 2), Frac(0, 1))
        self.assertEqual(Frac(-1, 2) + 120, Frac(239, 2))
        self.assertEqual(Frac(-1, 2) + 0.5, Frac(0, 1))
        self.assertEqual(Frac(-1, 2) + 9.5, Frac(9, 1))
        self.assertEqual(9.5 + Frac(-1, 2), Frac(9, 1))

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 2) - Frac(1, 2), Frac(0, 1))
        self.assertEqual(Frac(1, 1) - 2, Frac(-1, 1))
        self.assertEqual(Frac(1, 1) - 0.25, Frac(3, 4))
        self.assertEqual(Frac(1, 2) - 0.25, Frac(1, 4))

    def test_mul_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 4), Frac(1, 8))
        self.assertEqual(Frac(1, 1) * Frac(1, 4), Frac(1, 4))
        self.assertEqual(Frac(1, 1) * 2, Frac(2, 1))
        self.assertEqual(Frac(1, 1) * 0.25, Frac(1, 4))
        self.assertEqual(Frac(1, 2) * 0.25, Frac(1, 8))

    def test_div_frac(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        self.assertEqual(Frac(1, 1) / Frac(1, 4), Frac(4, 1))
        self.assertEqual(Frac(1, 1) / 2, Frac(1, 2))
        self.assertEqual(Frac(1, 1) / 0.25, Frac(4, 1))

    def test_pos(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))

    def test_neg(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(0, 1), Frac(0, 2))
        self.assertEqual(-Frac(-3, 2), Frac(3, 2))

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), float(1 / 2))
        self.assertEqual(float(Frac(0, 1)), float(0 / 1))
        self.assertEqual(float(Frac(-3, 2)), float(-3 / 2))

    def test_invert(self):
        self.assertEqual(~(Frac(1, 2)), Frac(2, 1))
        self.assertEqual(~(Frac(0, 1)), Frac(0, 1))
        self.assertEqual(~(Frac(7, 2)), Frac(2, 7))

    def test_hash(self):
        self.assertEqual(hash(Frac(1, 2)), hash(Frac(1, 2)))
        self.assertEqual(hash(Frac(0, 1)), hash(Frac(0, 1)))
        self.assertEqual(hash(Frac(4, 4)), hash(Frac(4, 4)))
        self.assertEqual(hash(Frac(1, 2)), hash(Frac(1, 2)))


if __name__ == '__main__':
    unittest.main()
