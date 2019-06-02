from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Checks that first string is anagram of second, return boolean

    :param s: String
    :param t: String
    :return: Boolean
    """

    if len(s) != len(t):
        return False

    counter = Counter(s)

    for char in t:

        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True
