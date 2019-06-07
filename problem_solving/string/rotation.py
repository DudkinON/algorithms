def string_rotation(s: str, t: str) -> bool:
    """
    Checks that string 't' is rotation of string 's'

    :param s: String
    :param t: String
    :return: Boolean
    """
    return (s + s).find(t) != -1 if len(s) == len(t) > 0 else False
