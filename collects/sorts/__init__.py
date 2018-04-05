from sys import stdin

counter = 0


def sort(l):

    q = []
    c = 0

    for i in range(len(l)):
        if l[i] < l[i + 1]:
            print(l[i])
    return q


def main():
    stdin.readline().split()
    unsorted = [[int(n)] for n in stdin.readline().split()]
    # assert amount == len(unsorted)
    print(sort(unsorted))
    # print(counter)


if __name__ == '__main__':
    main()
