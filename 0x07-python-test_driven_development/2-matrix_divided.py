#!/usr/bin/python3
def matrix_divided(matrix, div):
    errMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errMsg)
    if not isinstance(matrix, list):
        raise TypeError(errMsg)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errMsg)
        for items in lists:
            if not isinstance(items, int) and not isinstance(items, float):
                raise TypeError(errMsg)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errMsg)
        if not all(len(lists) == len(matrix[0]) for lists in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        if div == 0:
            raise ZeroDivisionError("division by zero")
    return ([[round(items / div, 2) for items in lists] for lists in matrix])
