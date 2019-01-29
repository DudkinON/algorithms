from unittest import TestCase
from collects.recursion import factorial, fibonacci, invert_string


class TestRecursionFunction(TestCase):

    def test_factorial(self):
        self.assertEqual(120, factorial(5))
        self.assertEqual(0, factorial(0))
        self.assertEqual(1, factorial(1))

    def test_fibonacci(self):
        self.assertEqual(5, fibonacci(5))
        self.assertEqual(2, fibonacci(3))
        self.assertEqual(21, fibonacci(8))

    def test_invert_string(self):
        self.assertEqual("gnirts elpmis", invert_string("simple string"))
        self.assertEqual("a", invert_string("a"))
        self.assertEqual("", invert_string(""))
