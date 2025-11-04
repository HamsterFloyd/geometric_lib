import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)


def area(a, b):
    #Функция принимает на вход две стороны, возвращает площадь прямоугольника
    return a * b

def perimeter(a, b):
    #Функция принимает на вход две стороны, возвращает периметр прямоугольника
    return (a+b)*2
