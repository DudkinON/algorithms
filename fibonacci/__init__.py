def get_fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return get_fibonacci_recursion(n - 1) + get_fibonacci_recursion(n - 2)

