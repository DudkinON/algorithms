def russian_peasants(a, b):
    if a < 0 < b or b < 0 < a:
        positive = False
    else:
        positive = True
    x, y, z = abs(a), abs(b), 0
    while x > 0:
        if x % 2 == 1:
            z += y
        y = y << 1
        x = x >> 1
    return z if positive else -z


def main():
    a, b = [int(numbs) for numbs in raw_input().split()]
    print russian_peasants(a, b)


if __name__ == '__main__':
    main()
