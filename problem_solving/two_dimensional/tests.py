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

    def test_mine_sweeper(self):
        result1 = mine_sweeper([[0, 2], [2, 0]], 3, 3)
        a1 = [[0, 1, -1],
              [1, 2, 1],
              [-1, 1, 0]]
        result2 = mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)
        a2 = [[-1, -1, 2, 1],
              [2, 3, -1, 1],
              [0, 1, 1, 1]]
        result3 = mine_sweeper([[1, 1], [1, 2],
                                [2, 2], [4, 3]], 5, 5)
        a3 = [[1, 2, 2, 1, 0],
              [1, -1, -1, 2, 0],
              [1, 3, -1, 2, 0],
              [0, 1, 2, 2, 1],
              [0, 0, 1, -1, 1]]

        self.assertEqual(result1, a1)
        self.assertEqual(result2, a2)
        self.assertEqual(result3, a3)

    def test_bfs(self):

        grid = [
            [0, 0, 0, 0, 9, 0, 0],
            [0, 9, 9, 0, 0, 0, 0],
            [0, 0, 9, 0, 9, 0, 0],
            [0, 9, 9, 0, 9, 0, 9],
            [0, 9, 1, 0, 0, 0, 0],
        ]

        a1 = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4)]
        a2 = [(5, 3), (5, 4), (4, 4), (3, 4), (2, 4)]

        self.assertEqual(bfs(grid, (0, 0)), a1)
        self.assertEqual(bfs(grid, (5, 3)), a2)
