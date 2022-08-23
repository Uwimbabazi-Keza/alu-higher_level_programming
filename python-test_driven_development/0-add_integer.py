#!/usr/bin/python3
"""
Module containing function that adds two integers
"""


def add_integer(a, b=98):
    """
    adds two integers
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return a+b
