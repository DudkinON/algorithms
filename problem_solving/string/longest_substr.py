def longest_substr(s: str) -> int:

    max_len, sub = 0, ""

    for char in s:
        if char not in sub:
            sub += char
        else:
            sub = sub[sub.find(char) + 1:]
            sub += char

        max_len = len(sub) if len(sub) > max_len else max_len

    return max_len
