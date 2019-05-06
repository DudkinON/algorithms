from unittest import TestCase
from problem_solving.two_dimensional import rotate


class TwoDimensionalTests(TestCase):

    def test_rotate(self):
        arr1 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        a1 = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]

        arr2 = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]

        a2 = [[13, 9, 5, 1],
              [14, 10, 6, 2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]]

        self.assertEqual(rotate(arr1, len(arr1)), a1)
        self.assertEqual(rotate(arr2, len(arr2)), a2)
