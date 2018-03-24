from unittest import TestCase
from greedy_algorithms.continuous_backpack import *


class TestCover(TestCase):

    def test_cover_segments(self):
        segments = [[60, 20], [100, 50], [120, 30]]
        self.assertEqual(max_price([3, 50], segments), 180)
