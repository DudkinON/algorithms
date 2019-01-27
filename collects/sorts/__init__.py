from sys import stdin


def bubble_sort(lst):
    """
    Implementation of bubble sort algorithm

    :param lst: list
    :return: sorted list
    """
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


def merge(a, b):

    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(a) and right_index < len(b):
        if a[left_index] < b[right_index]:
            merged_list.append(a[left_index])
            left_index += 1
        else:
            merged_list.append(b[right_index])
            right_index += 1

    return merged_list + a[left_index:] + b[right_index:]


def merge_sort(lst):

    if len(lst) < 2:
        return lst

    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]

    return merge(merge_sort(left), merge_sort(right))


def main():
    print("Enter numbers separated with whitespace: ")
    unsorted = [int(n) for n in stdin.readline().split()]
    print("unsorted list:\t", unsorted)
    print("bubble_sort:\t", bubble_sort(unsorted))
    print("selection_sort:\t", selection_sort(unsorted))
    print("insertion_sort:\t", insertion_sort(unsorted))
    print("merge_sort:\t\t", merge_sort(unsorted))


if __name__ == '__main__':
    main()
