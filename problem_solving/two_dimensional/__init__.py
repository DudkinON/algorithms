from copy import deepcopy


def rotate(arr, n):

    rotated = deepcopy(arr)

    for i in range(n):
        for j in range(n):
            (new_i, new_j) = (j, n - 1 - i)
            rotated[new_i][new_j] = arr[i][j]

    return rotated
