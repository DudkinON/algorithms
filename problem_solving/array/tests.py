from unittest import TestCase
from problem_solving.array.three_sum import three_sum


class TestArrays(TestCase):
    def test_three_sum(self):
        arr1 = [-1, 0, 1, 2, -1, -4]
        arr2 = []
        arr3 = [0]
        arr4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(three_sum(arr1), [[-1, 0, 1], [-1, -1, 2]])
        self.assertEqual(three_sum(arr2), [])
        self.assertEqual(three_sum(arr3), [])
        self.assertEqual(three_sum(arr4), [[0, 0, 0]])
