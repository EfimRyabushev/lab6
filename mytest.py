# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib
import math

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.sqrt(9), 3)
        self.assertEqual(lib.sqrt(1), 1)
        self.assertEqual(lib.sqrt(0), 0)

    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.sqrt(-1), 0)
    def test_even_positive_even(self):
        self.assertEqual(lib.even(2), True)
        self.assertEqual(lib.even(0), True)
    def test_even_negative_even(self):
        self.assertEqual(lib.even(-2), True)
    def test_even_positive_noneven(self):
        self.assertEqual(lib.even(1), False)
    def test_even_negative_noneven(self):
        self.assertEqual(lib.even(-1), False)
    def test_factorial_negative(self):
        self.assertEqual(lib.factorial(-1), 1)
    def test_factorial_positive(self):
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(3), 3 * lib.factorial(2))
    def test_palindrome(self):
        self.assertEqual(lib.palindrome(""), True)
        self.assertEqual(lib.palindrome("aa"), True)
        self.assertEqual(lib.palindrome("aba"), True)
        self.assertEqual(lib.palindrome("ab"), False)
    def test_prime(self):
        self.assertEqual(lib.prime(2), True)
        self.assertEqual(lib.prime(1), True)
        self.assertEqual(lib.prime(4), False)
        self.assertEqual(lib.prime(9), False)
    def test_sin(self):
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin(1), math.sin(1))

unittest.main(verbosity=2)

