def string_compression(s: str) -> str:

    if not len(s):
        return s

    result = s[0]
    counter = 1

    for i in range(1, len(s)):
        if s[i] != result[-1]:
            result += str(counter)
            result += s[i]
            counter = 1
        else:
            counter += 1
    result += str(counter)
    return result if len(result) < len(s) else s