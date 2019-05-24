from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams and returns them

    :param strs: List[str]
    :return: List[List[str]]
    """

    _map = {}

    for item in strs:

        _hash = ''.join(sorted(item))

        if _map.get(_hash) is None:
            _map[_hash] = []
        _map[_hash].append(item)

    return list(_map.values())
