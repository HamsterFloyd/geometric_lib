import math

import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_ten_mul(self):
        res = area(10)
        self.assertEqual(res, 100)



def area(r):
    #Функция принимает на вход радиус, возвращает площадь круга
    return math.pi * r * r


def perimeter(r):
    #Функция принимает на вход радиус, возвращает периметр круга
    return 2 * math.pi * r

