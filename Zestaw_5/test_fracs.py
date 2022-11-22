import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])
        self.assertEqual(add_frac([0, 2], [0, 2]), [0, 1])
        self.assertEqual(add_frac([0, 2], [4, 2]), [2, 1])
        self.assertEqual(add_frac([6, 10], [-6, 8]), [-3, 20])
        self.assertRaises(ValueError, add_frac, [-1, 0], [1, 0])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), [0, 1])
        self.assertEqual(sub_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(sub_frac([0, 2], [0, 2]), [0, 1])
        self.assertEqual(sub_frac([0, 2], [4, 2]), [-2, 1])
        self.assertEqual(sub_frac([0, 2], [-4, -2]), [-2, 1])
        self.assertRaises(ValueError, sub_frac, [-1, 0], [1, 0])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 4]), [1, 8])
        self.assertEqual(mul_frac([0, 2], [1, 3]), [0, 1])
        self.assertEqual(mul_frac([3, 2], [1, 1]), [3, 2])
        self.assertEqual(mul_frac([-1, 2], [1, -4]), [1, 8])
        self.assertEqual(mul_frac([5, 3], [-4, 2]), [-10, 3])
        self.assertRaises(ValueError, mul_frac, [-1, 0], [1, 0])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])
        self.assertEqual(div_frac([0, 2], [1, 3]), [0, 1])
        self.assertEqual(div_frac([3, 2], [1, 1]), [3, 2])
        self.assertEqual(div_frac([-1, 2], [1, -4]), [2, 1])
        self.assertEqual(div_frac([5, 3], [-4, 2]), [-5, 6])
        self.assertRaises(ValueError, div_frac, [-1, 0], [1, 0])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 1]))
        self.assertTrue(is_positive([-1, -1]))
        self.assertFalse(is_positive([-1, 1]))
        self.assertFalse(is_positive([1, -1]))
        self.assertRaises(ValueError, is_positive, [-1, 0])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 1]))
        self.assertRaises(ValueError, is_zero, [1, 0])

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 4]), 1)
        self.assertEqual(cmp_frac([0, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([3, 2], [6, 4]), 0)
        self.assertRaises(ValueError, cmp_frac, [1, 0], [1, 1])

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), float(1/2))
        self.assertEqual(frac2float([0, 2]), float(0))
        self.assertEqual(frac2float([3, 2]), float(3/2))
        self.assertRaises(ValueError, frac2float, [1, 0])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
