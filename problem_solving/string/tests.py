from unittest import TestCase
from problem_solving.string.longest_substr import longest_substr
from problem_solving.string.roman import roman_to_int


class TestStringFunctions(TestCase):
    def test_longest_substr(self):
        self.assertEqual(longest_substr("abcabcbb"), 3)
        self.assertEqual(longest_substr("bbb"), 1)
        self.assertEqual(longest_substr("abba"), 2)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("LIV"), 54)
        self.assertEqual(roman_to_int("CLVII"), 157)
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
