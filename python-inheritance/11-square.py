#!/usr/bin/python3
"""Module: Task 11, class Square inherits from Rectangle class Task 9"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square"""

    def __init__(self, size):
        """initialize"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size * self.__size

    def __str__(self):
        """returns str"""
        return "[Square] {}/{}".format(self.__size, self.__size)
