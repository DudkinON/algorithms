from queue import Queue
from copy import deepcopy
from math import ceil, floor
from collections import deque
from typing import List


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


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate a matrix 90 degrees clockwise

    :param matrix: List[List[int]]
    :return: List[List[int]]
    """

    for layer in range(len(matrix) // 2):
        for i in range(layer, len(matrix) - layer - 1):

            # save a first element
            first = matrix[layer][i]

            # rewrite first element with forth element
            matrix[layer][i] = matrix[-i - 1][layer]

            # rewrite fourth element with forth third element
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # rewrite third element with second element
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # rewrite second element with first element
            matrix[i][-layer - 1] = first

    return matrix


def rotate_less_memory(arr, n):
    """
    Rotate two dimensional array by 90 degrees with additional
    memory space complexity O(1)

    :param arr: List[List[int]] - two dimensional array
    :param n: Integer - size of array
    :return: List[List[int]] - two dimensional array
    """

    # Put to the new array new numbers
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


def click(field, nr, nc, x, y):
    """
    Depends on the coordinates x and y or fills all
    related empty fields with - 2 or returns the array
    without changes

    :param field: List[List[int]] - Field of mines
    :param nr: Integer - number of rows
    :param nc: Integer - number of columns
    :param x: Integer - x by X direction
    :param y: Integer - y by Y direction
    :return: List[List[int]] - Field of mines
    """

    # Create a queue
    queue = Queue()

    # If a coordinate is 0 add to the queue and change value to -2
    if field[x][y] == 0:
        field[x][y] = -2
        queue.put((x, y))

    while not queue.empty():
        x, y = queue.get()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < nr and nc > j >= 0 == field[i][j]:
                    field[i][j] = -2
                    queue.put((i, j))

    return field


def mine_sweeper(bombs, num_rows, num_cols):
    """
    Generates mine field with given data

    :param bombs: List[List[int]] - represent list of bombs coordinates
    :param num_rows: Integer - number of rows
    :param num_cols: Integer - number of columns
    :return: List[List[int]] - 2D array
    """

    # Generate empty two dimensional array
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    # fill it up with bombs as -1 and numbers around
    for bomb in bombs:
        (x, y) = bomb
        field[x][y] = -1
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < num_rows \
                        and 0 <= j < num_cols \
                        and field[i][j] != -1:
                    field[i][j] += 1
    return field


def bfs(_grid, start):
    """
    Finds and returns shortest path

    :param _grid: List[List[int]]2D array
    :param start: Tuple(int) - Start position
    :return: List[Tuple(int)] - Shortest path
    """

    queue = deque([[start]])
    seen = {}

    def get_id(_x, _y):
        return "{}_{}".format(_x, _y)

    while queue:
        _path = queue.popleft()
        x, y = _path[-1]

        if _grid[y][x] == 1:
            return _path

        for _x, _y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

            if 0 <= _x < len(_grid[0]) \
                    and 0 <= _y < len(_grid) \
                    and _grid[_y][_x] != 9 \
                    and seen.get(get_id(_x, _y)) is None:
                queue.append(_path + [(_x, _y)])
                seen[get_id(_x, _y)] = (_x, _y)
