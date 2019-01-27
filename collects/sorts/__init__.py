from sys import stdin


def bubble_sort(lst):

    length = len(lst)

    if length < 2:
        return lst

    for i in range(length):
        for j in range(length - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


def selection_sort(lst):

    length = len(lst)

    if length < 2:
        return lst

    for i in range(length):
        smallest = i
        temp = lst[i]
        for j in range(i + 1, length):
            if lst[smallest] > lst[j]:
                smallest = j
        lst[i] = lst[smallest]
        lst[smallest] = temp

    return lst


def insertion_sort(lst):

    length = len(lst)

    if length < 2:
        return lst

    for i in range(length):
        if lst[i] < lst[0]:
            lst = [lst[i]] + lst[:i] + lst[i + 1:]
        else:
            for j in range(1, i):
                if lst[j - 1] <= lst[i] < lst[j]:
                    lst = lst[:j] + [lst[i]] + lst[j:i] + lst[i + 1:]

    return lst


def main():
    print("Enter numbers separated with whitespace: ")
    unsorted = [int(n) for n in stdin.readline().split()]
    print("unsorted list:\t", unsorted)
    print("bubble_sort:\t", bubble_sort(unsorted))
    print("selection_sort:\t", selection_sort(unsorted))
    print("insertion_sort:\t", insertion_sort(unsorted))


if __name__ == '__main__':
    main()
