#!/usr/bin/python3
"""
Module containing a function that divides
all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    checks if args are numbers
    checks if size of each row of matrix is equal
    checks if div is 0
    divides elements of matrix
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or (len(matrix) == 0) \
            or type(matrix[0]) is not list or (len(matrix[0]) == 0):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        for n in i:
            if type(n) is not int and type(n) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for i in matrix:
        row = []
        for n in i:
            element = round((n/div), 2)
            row.append(element)
        new_matrix.append(row)
    return new_matrix
