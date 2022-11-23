from points import *

import unittest


class TestPoints(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(1, 2)), '(1, 2)')
        self.assertEqual(str(Point(0, 0)), '(0, 0)')
        self.assertEqual(str(Point(4, 4)), '(4, 4)')

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), 'Point(1, 2)')
        self.assertEqual(repr(Point(0, 0)), 'Point(0, 0)')
        self.assertEqual(repr(Point(4, 4)), 'Point(4, 4)')

    def test_eq(self):
        self.assertEqual(Point(1, 2) == Point(1, 2), True)
        self.assertEqual(Point(0, 0) == Point(0, 0), True)
        self.assertEqual(Point(4, 4) == Point(4, 4), True)
        self.assertEqual(Point(1, 2) == Point(2, 3), False)
        self.assertEqual(Point(0, 0) == Point(0, 2), False)
        self.assertEqual(Point(4, 4) == Point(4, 0), False)

    def test_ne(self):
        self.assertEqual(Point(1, 2) != Point(1, 2), False)
        self.assertEqual(Point(0, 0) != Point(0, 0), False)
        self.assertEqual(Point(4, 4) != Point(4, 4), False)
        self.assertEqual(Point(1, 2) != Point(2, 3), True)
        self.assertEqual(Point(0, 0) != Point(0, 2), True)
        self.assertEqual(Point(4, 4) != Point(4, 0), True)

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(1, 2), Point(2, 4))
        self.assertEqual(Point(0, 0) + Point(0, 0), Point(0, 0))
        self.assertEqual(Point(4, 4) + Point(4, 4), Point(8, 8))
        self.assertEqual(Point(1, 2) + Point(2, 3), Point(3, 5))
        self.assertEqual(Point(0, 0) + Point(0, 2), Point(0, 2))
        self.assertEqual(Point(4, 4) + Point(4, 0), Point(8, 4))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(1, 2), Point(0, 0))
        self.assertEqual(Point(0, 0) - Point(0, 0), Point(0, 0))
        self.assertEqual(Point(4, 4) - Point(4, 4), Point(0, 0))
        self.assertEqual(Point(1, 2) - Point(2, 3), Point(-1, -1))
        self.assertEqual(Point(0, 0) - Point(0, 2), Point(0, -2))
        self.assertEqual(Point(4, 4) - Point(8, 6), Point(-4, -2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(1, 2), 5)
        self.assertEqual(Point(0, 0) * Point(0, 0), 0)
        self.assertEqual(Point(4, 4) * Point(4, 4), 32)
        self.assertEqual(Point(1, 2) * Point(2, 3), 8)
        self.assertEqual(Point(0, 0) * Point(0, 2), 0)
        self.assertEqual(Point(4, 4) * Point(-2, 6), 16)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(1, 2)), 0)
        self.assertEqual(Point(0, 0).cross(Point(0, 0)), 0)
        self.assertEqual(Point(4, 4).cross(Point(4, 4)), 0)
        self.assertEqual(Point(1, 2).cross(Point(2, 3)), -1)
        self.assertEqual(Point(0, 0).cross(Point(0, 2)), 0)
        self.assertEqual(Point(4, 4).cross(Point(-2, 6)), 32)

    def test_length(self):
        self.assertEqual(Point(1, 2).length(), 3**0.5)
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(4, 4).length(), 8**0.5)
        self.assertEqual(Point(2, 2).length(), 2)
        self.assertEqual(Point(0, 16).length(), 4)
        self.assertEqual(Point(4, 4).length(), 8**0.5)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))
        self.assertEqual(hash(Point(0, 0)), hash(Point(0, 0)))
        self.assertEqual(hash(Point(4, 4)), hash(Point(4, 4)))
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))


if __name__ == '__main__':
    unittest.main()
