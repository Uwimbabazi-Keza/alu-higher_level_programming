#!/usr/bin/python3
"""Module: 9 Full rectangle, inherits from task 7 based on task 8"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inheritance BaseGeometry"""

    def __init__(self, width, height):
        """initialize object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
