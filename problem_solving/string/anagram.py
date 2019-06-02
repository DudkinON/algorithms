from collections import Counter


def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    counter = Counter(s)

    for char in t:

        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True
