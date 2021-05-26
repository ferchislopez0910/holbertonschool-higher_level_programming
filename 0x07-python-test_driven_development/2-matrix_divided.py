#!/usr/bin/python3
"""
function that divides all elements of a matrix..
return new_matrix

"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    new_matrix = []
    ln = len(matrix[0])
    x = "matrix must be a matrix (list of lists of integers/floats"

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        new_list = []
        if len(row) == ln:
            for column in row:
                if type(column) is int or type(column) is float:
                    divide = column / div
                    new_list.append(round(divide, 2))
                else:
                    raise TypeError(x)
            new_matrix.append(new_list)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
