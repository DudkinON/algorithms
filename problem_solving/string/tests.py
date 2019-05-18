from unittest import TestCase
from problem_solving.string.longest_substr import longest_substr


class TestStringFunctions(TestCase):
    def test_longest_substr(self):
        self.assertEqual(longest_substr("abcabcbb"), 3)
        self.assertEqual(longest_substr("bbb"), 1)
        self.assertEqual(longest_substr("abba"), 2)
