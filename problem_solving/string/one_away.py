def one_away(s: str, t: str) -> bool:
    """
    Checks if a string can converted to another string with a single edit

    :param s: String
    :param t: String
    :return: Boolean
    """
    
    len_diff = abs(len(s) - len(t))

    if len_diff > 1:
        return False

    elif len_diff == 0:
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += 1
                if diff > 1:
                    return False
        return True

    else:
        max_s = s if len(s) > len(t) else t
        min_s = t if len(s) > len(t) else s

        diff = i = j = 0

        while i < len(min_s) and j < len(max_s):
            if min_s[i] != max_s[j]:
                diff += 1
                j += 1
                if diff > 1:
                    return False
            else:
                j += 1
                i += 1

        return True
