from geometric_lib import *
import unittest

class TestRectangle(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_rect_mul(self):
        res = rectangle_area(10, 20)
        self.assertEqual(res, 200)


    def test_ten_per(self):
        res = rectangle_perimeter(10, 20)
        self.assertEqual(res, 60)
