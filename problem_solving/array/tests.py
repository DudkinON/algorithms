from unittest import TestCase
from problem_solving.array.three_sum import three_sum
from problem_solving.array.merge import merge


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

    def test_merge(self):
        case1 = [1, 2, 3, 0, 0, 0]
        case2 = [0, 0, 0, 0, 0]
        case3 = [4, 0, 0, 0, 0, 0]
        case4 = [1, 2, 4, 5, 6, 0]
        merge(case1, 3, [2, 5, 6], 3)
        merge(case2, 1, [1, 2, 4, 6], 4)
        merge(case3, 1, [1, 2, 3, 5, 6], 5)
        merge(case4, 5, [3], 1)

        self.assertEqual(case1, [1, 2, 2, 3, 5, 6])
        self.assertEqual(case2, [0, 1, 2, 4, 6])
        self.assertEqual(case3, [1, 2, 3, 4, 5, 6])
        self.assertEqual(case4, [1, 2, 3, 4, 5, 6])
