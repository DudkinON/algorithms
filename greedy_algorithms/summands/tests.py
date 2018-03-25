from unittest import TestCase
from greedy_algorithms.summands import summands


class TestSummands(TestCase):
    def test_summands(self):
        self.assertEqual(summands(4), [1, 3])
        self.assertEqual(summands(6), [1, 2, 3])
