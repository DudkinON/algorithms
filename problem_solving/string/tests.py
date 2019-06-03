from unittest import TestCase
from problem_solving.string.longest_substr import longest_substr
from problem_solving.string.roman import roman_to_int
from problem_solving.string.str2int import str_to_int
from problem_solving.string.unique import is_unique
from problem_solving.string.anagram import is_anagram
from problem_solving.string.url import urlify
from problem_solving.string.anagram import pal_anagram
from problem_solving.string.one_away import one_away


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

    def test_urlify(self):
        self.assertEqual(urlify("Mr John Doe   ", 11), "Mr%20John%20Doe")
        self.assertEqual(urlify("John + Doe   ", 10), "John%20+%20Doe")
        self.assertEqual(urlify("  ", 1), "%20")
        self.assertEqual(urlify(" !  ", 2), "%20!")
        self.assertEqual(urlify("", 0), "")

    def test_pal_anagram(self):
        data = [
            ('Tact Coa', True),
            ('jhsabckuj ahjsbckj', True),
            ('Able was I ere I saw Elba', True),
            ('So patient a nurse to nurse a patient so', False),
            ('Random Words', False),
            ('Not a Palindrome', False),
            ('no x in nixon', True),
            ('azAZ', True)]

        for [test_string, expected] in data:
            actual = pal_anagram(test_string)
            self.assertEqual(actual, expected)

    def test_one_away(self):
        data = [
            ('pale', 'ple', True),
            ('pales', 'pale', True),
            ('pale', 'bale', True),
            ('paleabc', 'pleabc', True),
            ('pale', 'ble', False),
            ('a', 'b', True),
            ('', 'd', True),
            ('d', 'de', True),
            ('pale', 'pale', True),
            ('pale', 'ple', True),
            ('ple', 'pale', True),
            ('pale', 'bale', True),
            ('pale', 'bake', False),
            ('pale', 'pse', False),
            ('ples', 'pales', True),
            ('pale', 'pas', False),
            ('pas', 'pale', False),
            ('pale', 'pkle', True),
            ('pkle', 'pable', False),
            ('pal', 'palks', False),
            ('palks', 'pal', False)
        ]
        for [test_s1, test_s2, expected] in data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)
