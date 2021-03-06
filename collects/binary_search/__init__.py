from sys import stdin


def binary_search(pool, target):
    """
    Search a digit in sorted list of numbers
    if find return index else return -1

    :param pool: list of integers
    :param target: int
    :return: index
    """
    pool_length = len(pool)

    # filter if value more or less when max and min in list
    if pool_length < 1 or target < pool[0] or target > pool[-1]:
        return -1

    left, right = 0, pool_length

    while left < right:

        mid = int((left + right) / 2)

        if target < pool[mid]:
            right = mid
        elif target > pool[mid]:
            left = mid + 1
        else:
            return mid

    return -1


def main():
    pool = [int(char) for char in stdin.readline().split()]
    targets = [int(char) for char in stdin.readline().split()]

    results = []

    for target in targets:
        results.append(binary_search(pool, target))

    print(" ".join(str(v) for v in results))


if __name__ == '__main__':
    main()
