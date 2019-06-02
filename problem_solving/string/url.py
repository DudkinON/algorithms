def urlify(s: str, length: int) -> str:
    """
    Replaces single spaces with %20 and fills in trailing spaces

    :param s: String
    :param length: Integer
    :return: String
    """

    index = len(s)

    for i in range(length - 1, -1, -1):

        if s[i] == ' ':
            # Replace space
            s = s[:index - 2] + '%20' + s[index + 1:] if length > 2 else '%20' + s[index + 1:]
            index -= 3
        else:
            # Move character
            s = s[:index] + s[i] + s[index+1:]
            index -= 1
    return s
