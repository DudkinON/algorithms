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


def pal_anagram(s: str) -> bool:
    """
    Checks that string is a permutation of palindrome

    :param s: String
    :return: Boolean
    """
    _map = [0 for _ in range(ord('z') - ord('a') + 1)]

    a, z, A, Z = ord('a'), ord('z'), ord('A'), ord('Z')

    odds = 0

    for char in s:
        val = ord(char)

        if a <= val <= z:
            index = val - a
        elif A <= val <= Z:
            index = val - A
        else:
            index = -1

        if index > -1:
            _map[index] += 1

            if _map[index] % 2 == 1:
                odds += 1
            else:
                odds -= 1

    return odds < 2
