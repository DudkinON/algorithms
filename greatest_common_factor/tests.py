from unittest import TestCase
from greatest_common_factor import *


class TestGCF(TestCase):

    def test_euclid_gcf(self):
        self.assertEqual(euclid_algorithm_gcf(3918848, 1653264), 61232)
        self.assertEqual(euclid_algorithm_gcf(14159572, 63967072), 4)
        self.assertEqual(euclid_algorithm_gcf(12, 8), 4)
        self.assertEqual(euclid_algorithm_gcf(12, 0), 12)
        self.assertEqual(euclid_algorithm_gcf(0, 8), 8)
