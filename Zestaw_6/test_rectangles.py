from rectangles import Rectangle
from points import Point
import unittest


class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(0, 0, 4, 4)), "[(0, 0), (4, 4)]")
        self.assertEqual(str(Rectangle(1, 2, 4, 4)), "[(1, 2), (4, 4)]")
        self.assertEqual(str(Rectangle(3, 3, 0, 0)), "[(3, 3), (0, 0)]")
        self.assertEqual(str(Rectangle(0, 4.2, 8.6, 0)), "[(0, 4.2), (8.6, 0)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(0, 0, 4, 4)), "Rectangle(0, 0, 4, 4)")
        self.assertEqual(repr(Rectangle(1, 2, 4, 4)), "Rectangle(1, 2, 4, 4)")
        self.assertEqual(repr(Rectangle(3, 3, 0, 0)), "Rectangle(3, 3, 0, 0)")
        self.assertEqual(repr(Rectangle(0, 4.2, 8.6, 0)), "Rectangle(0, 4.2, 8.6, 0)")

    def test_eq(self):
        self.assertTrue(Rectangle(0, 0, 4, 4) == Rectangle(0, 0, 4, 4))
        self.assertTrue(Rectangle(1, 2, 4, 4) == Rectangle(1, 2, 4, 4))
        self.assertFalse(Rectangle(3, 3, 0, 0) == Rectangle(3, 3, 0, 0.001))
        self.assertFalse(Rectangle(4, 3, 2, 1) == Rectangle(3, 3, 0, 0))

    def test_ne(self):
        self.assertFalse(Rectangle(0, 0, 4, 4) != Rectangle(0, 0, 4, 4))
        self.assertFalse(Rectangle(1, 2, 4, 4) != Rectangle(1, 2, 4, 4))
        self.assertTrue(Rectangle(3, 3, 0, 0) != Rectangle(3, 3, 0, 0.001))
        self.assertTrue(Rectangle(4, 3, 2, 1) != Rectangle(3, 3, 0, 0))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).center(), Point(2.0, 2.0))
        self.assertEqual(Rectangle(1, 2, 4, 4).center(), Point(2.5, 3.0))
        self.assertEqual(Rectangle(3, 3, 0, 0).center(), Point(1.5, 1.5))
        self.assertEqual(Rectangle(0, 4.2, 8.6, 0).center(), Point(4.3, 2.1))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).area(), 16)
        self.assertEqual(Rectangle(1, 2, 4, 4).area(), 6)
        self.assertEqual(Rectangle(3, 3, 0, 0).area(), 9)
        self.assertEqual(Rectangle(0, 4.2, 8.6, 0).area(), 36.12)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).move(1, 1), Rectangle(1, 1, 5, 5))
        self.assertEqual(Rectangle(2, 1, 6, 4).move(-1, -1), Rectangle(1, 0, 5, 3))
        self.assertEqual(Rectangle(2, 1, 6, 4).move(0, 0), Rectangle(2, 1, 6, 4))
        self.assertEqual(Rectangle(2, 1, 6, 4).move(10, 10), Rectangle(12, 11, 16, 14))


if __name__ == '__main__':
    unittest.main()
