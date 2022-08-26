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
        self.__width = width

    @property
    def height(self):
        """return height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets height attribute"""
        self.__height = height

    @property
    def x(self):
        """gets x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets x attribute"""
        self.__x = x

    @property
    def y(self):
        """gets y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y attribute"""
        self.__y = y
