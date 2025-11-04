import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_mul(self):
        res = area(10, 20)
        self.assertEqual(res, 100)


def area(a, h):
    #Функция принимает на вход основание и высоту, возвращает площадь треугольника
    return a * h / 2

def perimeter(a, b, c):
    #Функция принимает 3 стороны треугольника, возвращает периметр треугольника
    return a + b + c
