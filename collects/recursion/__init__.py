def factorial(number):
    """
    Recursive counting factorial of a given number

    :param number: (integer)
    :return: number (integer)
    """
    return number if number < 3 else number * factorial(number - 1)


def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


def invert_string(s, result=""):
    if len(s) > 0:
        result += s[-1]
        return invert_string(s[:-1], result)
    else:
        return result
