def str_to_int(s: str) -> int:

    s, result = s.lstrip(), ""

    if s[0] == '-' or s[0] == '+':
        sign = s[0]
        s = s[1:]
    else:
        sign = ""

    _set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    for char in s:
        if char in _set:
            result += char
        else:
            break

    if len(result) == 0:
        return 0

    out = int(sign + result)
    out = -2147483648 if -2147483648 > out else out
    out = 2147483647 if 2147483647 < out else out

    return out
