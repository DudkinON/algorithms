from unittest import TestCase
from fibonacci import *


class TestFibonacci(TestCase):

    def test_recursion(self):
        self.assertEqual(get_fibonacci_recursion(0), 0)
        self.assertEqual(get_fibonacci_recursion(1), 1)
        self.assertEqual(get_fibonacci_recursion(2), 1)
        self.assertEqual(get_fibonacci_recursion(6), 8)
        self.assertEqual(get_fibonacci_recursion(10), 55)

    def test_loop_list(self):
        self.assertEqual(get_fibonacci_loop_list(0), 0)
        self.assertEqual(get_fibonacci_loop_list(1), 1)
        self.assertEqual(get_fibonacci_loop_list(2), 1)
        self.assertEqual(get_fibonacci_loop_list(6), 8)
        self.assertEqual(get_fibonacci_loop_list(10), 55)

    def test_loop_variables(self):
        self.assertEqual(get_fibonacci_loop_variables(0), 0)
        self.assertEqual(get_fibonacci_loop_variables(1), 1)
        self.assertEqual(get_fibonacci_loop_variables(2), 1)
        self.assertEqual(get_fibonacci_loop_variables(6), 8)
        self.assertEqual(get_fibonacci_loop_variables(10), 55)

    def test_fibonacci_rec_cache(self):
        self.assertEqual(get_fib_rec_cache(0), 0)
        self.assertEqual(get_fib_rec_cache(1), 1)
        self.assertEqual(get_fib_rec_cache(2), 1)
        self.assertEqual(get_fib_rec_cache(6), 8)
        self.assertEqual(get_fib_rec_cache(10), 55)
