def factorial(number):
    return number if number < 3 else number * factorial(number - 1)


def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
