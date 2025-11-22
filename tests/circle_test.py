from geometric_lib import *

import unittest

class TestCircle(unittest.TestCase):
    def test_zero_mul(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_ten_mul(self):
        res = circle_area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_ten_per(self):
        res = circle_perimeter(10)
        self.assertEqual(res, 62.83185307179586)
