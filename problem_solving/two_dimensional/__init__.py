from copy import deepcopy


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
