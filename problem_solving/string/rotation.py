def string_rotation(s: str, t: str) -> bool:

    return (s + s).find(t) != -1 if len(s) == len(t) > 0 else False
