def get_fibonacci_recursion(n):
    """
    Recursion function calculate Fibonacci number

    :param n: (Integer)
    :return: Integer
    """
    if n < 2:
        return n
    else:
        return get_fibonacci_recursion(n - 1) + get_fibonacci_recursion(n - 2)


def get_fibonacci_loop_list(n):
    """
    Calculate Fibonacci number use a loop and a list to store results

    :param n: (Integer)
    :return: Integer
    """
    fib_list = list()
    if n < 2:
        return n
    else:
        fib_list.append(0)
        fib_list.append(1)
        i = 2
        while i < n + 1:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            i += 1
    return fib_list[-1]


def get_fibonacci_loop_variables(n):
    """
    Calculate Fibonacci number use a loop and variables to store results

    :param n: (Integer)
    :return: Integer
    """
    result = 0
    if n < 2:
        return n
    else:
        first = 0
        second = 1
        i = 2
        while i < n + 1:
            result = first + second
            first = second
            second = result

            i += 1
    return result
