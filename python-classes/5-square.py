#!/usr/bin/python3
"""class square that prints area in #"""


class Square:
    """class that prints area of square in #"""

    def __init__(self, size=0):
        """Initialize"""
        self.__size = size

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size equals value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        def area(self):
            for i in range(self):
                a = '#'
                print(a*self)
        return area(self.__size)
