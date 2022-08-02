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
        if (type(value)) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints area"""
        def area(self):
        """gets area"""
            if self == 0:
                print()
            """accounts for 0"""
            else:
                for i in range(self):
                    a = '#'
                    print(a*self)
        return area(self.__size)
