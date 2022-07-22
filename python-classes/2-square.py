#!/usr/bin/python3
"""class type"""


class Square:
    """private instance attrivute size"""
    def __init__(self, size=0):
        """size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
