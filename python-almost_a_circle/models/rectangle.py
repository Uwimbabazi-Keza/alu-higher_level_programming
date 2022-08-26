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

    def display(self):
        """
        prints
        rectangle in #
        """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(self.__x * " " + '#' * self.__width)

    def __str__(self):
        """
        Returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>
        """
        s = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return (s)

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dictionary
        rep of Rectangle
        """
        dc = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        return dc
