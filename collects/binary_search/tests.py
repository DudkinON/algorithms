from unittest import TestCase
from collects.binary_search import *


class TestBinarySearch(TestCase):
    def test_binary_search(self):
        self.assertEqual(0, binary_search([1, 5, 8, 12, 13], 1))
        self.assertEqual(3, binary_search([1, 5, 8, 12, 13], 12))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 3))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 3))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 0))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 14))
