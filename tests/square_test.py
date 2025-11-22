from geometric_lib import *
import unittest

class TestSquare(unittest.TestCase):
    def test_zero_mul(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_ten_mul(self):
        res = square_area(10)
        self.assertEqual(res, 100)

    def test_ten_per(self):
        res = square_perimeter(10)
        self.assertEqual(res, 40)
