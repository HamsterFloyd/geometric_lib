from geometric_lib import *
import unittest

class TestTriangle(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_triangle_mul(self):
        res = triangle_area(10, 10)
        self.assertEqual(res, 50)

    def test_triangle_per(self):
        res = triangle_perimeter(10, 10, 32)
        self.assertEqual(res, 52)