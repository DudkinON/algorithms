from unittest import TestCase
from fibonacci import *


class TestFibonacci(TestCase):

    def test_recursion(self):
        self.assertEqual(get_fibonacci_recursion(0), 0)
        self.assertEqual(get_fibonacci_recursion(1), 1)
        self.assertEqual(get_fibonacci_recursion(2), 1)
        self.assertEqual(get_fibonacci_recursion(6), 8)
        self.assertEqual(get_fibonacci_recursion(10), 55)


