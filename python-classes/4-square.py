#!/usr/bin/python3
""""private attribute"""


class Square:
    """Private instance size for class square"""
    __size = None

    def __init__(self, size=0):
        """initilize size"""
        self.__size = size
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")

    def area(self):
        """area"""
        return (self.__size * self.__size)

    def set_size(self, value):
        """size"""
        if type(value) != int:
            raise Exception("size must be an integer")
        self.__size = value

    def get_size(self):
        """get size"""
        return self.__size

    size = property(get_size, set_size)
