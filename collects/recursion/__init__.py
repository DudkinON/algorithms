def factorial(number):
    return number if number < 3 else number * factorial(number - 1)
