from unittest import TestCase
from collects import sorts


class TestSortingAlgorithms(TestCase):

    def setUp(self):
        self.unsorted_list = [11, 24, 9, 18, 0, -1, 1, 4, 4, 5, 8, 3, 2, 7, 6]
        self.sorted_list = [-1, 0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 11, 18, 24]

    def test_bubble_sort(self):
        result = sorts.bubble_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, result)

    def test_selection_sort(self):
        result = sorts.selection_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, result)

    def test_insertion_sort(self):
        result = sorts.insertion_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, result)

    def test_merge_sort(self):
        result = sorts.merge_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, result)
