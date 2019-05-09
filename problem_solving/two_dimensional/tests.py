from unittest import TestCase
from problem_solving.two_dimensional import rotate, rotate_less_memory
from problem_solving.two_dimensional import click, mine_sweeper, bfs


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

    def test_rotate_less_memory(self):
        data1 = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

        a1 = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]

        data2 = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]

        a2 = [[13, 9, 5, 1],
              [14, 10, 6, 2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]]

        self.assertEqual(rotate_less_memory(data1, 3), a1)
        self.assertEqual(rotate_less_memory(data2, 4), a2)

    def test_click(self):
        arr1 = [[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, -1, 1, 0]]

        a1 = [[0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 1, -1, 1, 0]]

        a2 = [[-2, -2, -2, -2, -2],
              [-2, 1, 1, 1, -2],
              [-2, 1, -1, 1, -2]]

        arr2 = [[-1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, -1]]

        a3 = [[-1, 1, 0, 0],
              [1, 1, 0, 0],
              [0, 0, 1, 1],
              [0, 0, 1, -1]]

        a4 = [[-1, 1, -2, -2],
              [1, 1, -2, -2],
              [-2, -2, 1, 1],
              [-2, -2, 1, -1]]

        self.assertEqual(click(arr1, 3, 5, 2, 2), a1)
        self.assertEqual(click(arr1, 3, 5, 1, 4), a2)
        self.assertEqual(click(arr2, 4, 4, 0, 1), a3)
        self.assertEqual(click(arr2, 4, 4, 1, 3), a4)
