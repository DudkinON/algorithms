def is_unique(s: str) -> bool:
    """
    Check if all characters in the given string are unique

    :param s: String
    :return: Boolean
    """

    if len(s) > 128:
        return False

    unique_list = [False for _ in range(128)]

    for char in s:
        value = ord(char)
        if unique_list[value]:
            return False
        unique_list[value] = True

    return True
