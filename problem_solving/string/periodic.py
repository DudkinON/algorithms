def periodic(s: str) -> str:
    """
    Finds repetitive substring in given string

    :param s: String
    :return: String
    """

    if len(s) == 0:
        return ""

    period = s[0]

    for i in range(1, len(s)):

        period_length = len(period)
        start = len(s) - period_length
        end = start + period_length % len(s)

        if period == s[start:end]:

            while period == s[start:end] and start > 0:
                start -= period_length
                end = start + period_length

            if start == 0:
                return period

        period += s[i]

    return period
