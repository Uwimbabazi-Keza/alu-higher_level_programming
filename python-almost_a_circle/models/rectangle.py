#!/usr/bin/python3
"""Module contains sub-class Rectangle
inheriting from Base class
"""


from models.base import Base


class Rectangle(Base):
    """subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets width attribute"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """return height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets height attribute"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """gets x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets x attribute"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """gets y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y attribute"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area of rectangle"""
        return self.__width*self.__height
