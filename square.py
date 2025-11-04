import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_ten_mul(self):
        res = area(10)
        self.assertEqual(res, 100)


def area(a):
    #Функция принимает на вход сторону квадрата, возвращает его площадь
    return a * a


def perimeter(a):
    #Функция принимает на вход сторону квадрата, возвращает его периметр
    return 4 * a
