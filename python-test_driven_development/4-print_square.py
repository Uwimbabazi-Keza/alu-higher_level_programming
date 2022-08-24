#!/usr/bin/python3
"""
Module contains function that prints our a square
"""


def print_square(size):
    """
    prints square
    """
    if type(size) is not int:
            raise TypeError("size must be an integer")
    if size < 0:
            raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
            raise TypeError("size must be an integer")

    if size == 0:
        return None
    for i in range(size):
        for i in range(size):
            print('#', end='')
        print('')
