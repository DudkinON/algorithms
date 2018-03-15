def euclid_algorithm_gcf(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return euclid_algorithm_gcf(a % b, b)
    elif b >= a:
        return euclid_algorithm_gcf(a, b % a)
