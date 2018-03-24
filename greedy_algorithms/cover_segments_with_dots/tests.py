from unittest import TestCase
from greedy_algorithms.cover_segments_with_dots import *


class TestCover(TestCase):

    def test_cover_segments(self):
        segments = [[4, 7], [1, 3], [2, 5], [5, 6]]
        self.assertEqual(cover(segments), [3, 6])
