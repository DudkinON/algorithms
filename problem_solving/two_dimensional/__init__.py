from copy import deepcopy
from math import ceil, floor


def rotate(arr, n):
    """
    Rotate two dimensional array by 90 degrees with additional
    memory space complexity O(n) where n amaunt or elements in
    array

    :param arr: List[List[int]] - two dimensional array
    :param n: Integer - size of array
    :return: List[List[int]] - two dimensional array
    """

    # Create a copy of the array
    rotated = deepcopy(arr)

    # Put to the new array new numbers
    for i in range(n):
        for j in range(n):
            (new_i, new_j) = (j, n - 1 - i)
            rotated[new_i][new_j] = arr[i][j]

    return rotated


def rotate_less_memory(arr, n):

    for i in range(ceil(n/2)):
        for j in range(floor(n/2)):

            temp, new_i, new_j = [], i, j

            for k in range(4):
                temp.append(arr[new_i][new_j])
                new_i, new_j = new_j, n - 1 - new_i

            for k in range(4):
                arr[new_i][new_j] = temp[(k - 1) % 4]
                new_i, new_j = new_j, n - 1 - new_i

    return arr
