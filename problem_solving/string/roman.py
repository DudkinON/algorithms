def roman_to_int(s: str) -> int:
    """
    Converts a roman numeral to an integer

    :param s: String
    :return: Integer
    """

    cache = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = cache[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        value = cache[s[i]]
        if cache[s[i + 1]] > value:
            total -= value
        else:
            total += value
    return total
