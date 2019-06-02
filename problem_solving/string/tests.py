from unittest import TestCase
from problem_solving.string.longest_substr import longest_substr
from problem_solving.string.roman import roman_to_int
from problem_solving.string.str2int import str_to_int
from problem_solving.string.unique import is_unique
from problem_solving.string.anagram import is_anagram


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

    def test_str_to_int(self):
        self.assertEqual(str_to_int("-20 e"), -20)
        self.assertEqual(str_to_int("  -20"), -20)
        self.assertEqual(str_to_int(" 3-20"), 3)
        self.assertEqual(str_to_int("   -91283472332"), -2147483648)
        self.assertEqual(str_to_int("  91283472332"), 2147483647)

    def test_is_unique(self):
        self.assertEqual(is_unique("abcde"), True)
        self.assertEqual(is_unique("!@^4 abcde"), True)
        self.assertEqual(is_unique("_BRF4tr"), True)
        self.assertEqual(is_unique("  "), False)
        self.assertEqual(is_unique(" abracadabra"), False)
        self.assertEqual(is_unique("not unique string"), False)

    def test_is_anagram(self):
        self.assertEqual(is_anagram("abcd", "cbda"), True)
        self.assertEqual(is_anagram("bird", "rdbi"), True)
        self.assertEqual(is_anagram("The sky", "Tseh ky"), True)
        self.assertEqual(is_anagram("short one", "short on"), False)
        self.assertEqual(is_anagram("longer", "longer "), False)
        self.assertEqual(is_anagram("wrong", "vrong"), False)
