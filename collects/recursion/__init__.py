def factorial(number):
    """
    Recursive counting factorial of a given number

    :param number: (integer)
    :return: number (integer)
    """
    return number if number < 3 else number * factorial(number - 1)


def cache(f):
    """
    Function decorator, prevents unnecessary calling of the function.
    Improve performance (Time complexity) from O(2^n) to O(n), but
    increase Space complexity from O(1) to O(n).

    :param f: Function
    :return: Function
    """
    cache_data = {}

    def inner(n):
        if n not in cache_data:
            cache_data[n] = f(n)
        return cache_data[n]
    return inner


@cache
def fibonacci(n):
    """
    Recursive count Fibonacci number

    :param n: (integer)
    :return: number (integer)
    """
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


def invert_string(s, result=""):
    if len(s) > 0:
        result += s[-1]
        return invert_string(s[:-1], result)
    else:
        return result
