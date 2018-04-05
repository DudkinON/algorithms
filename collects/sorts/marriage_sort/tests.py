from unittest import TestCase
from collects.sorts.marriage_sort import *


class TestSort(TestCase):

    def test_marriage_sort(self):
        self.assertEqual([1, 2, 3, 4], marriage_sort([4, 3, 2, 1]))
        self.assertEqual([1, 2, 3, 4], marriage_sort([1, 3, 2, 4]))
        self.assertEqual([], marriage_sort([]))
        self.assertEqual([1], marriage_sort([1]))


