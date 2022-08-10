#!/usr/bin/python3
"""Area and
Perimeter
"""


class Rectangle:
    """
    class Rectangle: intializing height and width
    """
    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """
        gets
        width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"
        sets
        width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        gets
        height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets
        height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns
        area"""
        return self.__width*self.__height

    def perimeter(self):
        """returns
        perimeter"""
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return (self.__width*2)+(self.__height*2)

    def __str__(self):
        """
        returns
        rectangle in #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            c = '#'
            for i in range(self.__height-1):
                a = c*self.__width
                print(a)
            return a
