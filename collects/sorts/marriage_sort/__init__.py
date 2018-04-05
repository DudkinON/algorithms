from sys import stdin


def marriage(a, b):
    """
    Marriage of two sorted lists and return a new one

    :param a: list
    :param b: list
    :return: list
    """
    d = []
    while len(a) + len(b) > 0:
        len_a = len(a)
        len_b = len(b)
        if len_b > 0 and len_a > 0:
            if a[0] >= b[0]:
                d.append(b.pop(0))
            else:
                d.append(a.pop(0))

        elif len_a > 0 and len_b == 0:
            for x in a:
                d.append(a.pop(0))
        elif len_a == 0 and len_b > 0:
            for x in b:
                d.append(b.pop(0))
    return d


def marriage_sort(l):
    """
    Sort a list and return it

    :param l: list
    :return:
    """

    if len(l) < 2:
        return l

    q = []

    if type(l[0]) == int:
        while len(l) > 0:
            q.append([l.pop(0)])
    else:
        q = l

    while len(q) > 1:
        q.append(marriage(q.pop(0), q.pop(0)))

    return q[0]


def main():
    unsorted = [[int(n)] for n in stdin.readline().split()]
    print(marriage_sort(unsorted))


if __name__ == '__main__':
    main()
