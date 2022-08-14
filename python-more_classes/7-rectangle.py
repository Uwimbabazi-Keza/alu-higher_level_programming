#!/usr/bin/python3
"""
How many
instances
"""


class Rectangle:
    """
    class Rectangle
    """
    number_of_instances = 0  # initializes class attr
    print_symbol = '#'

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
            Rectangle.number_of_instances += 1

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
            c = "{}".format(self.print_symbol) * self.__width
            return'\n'.join(c for i in range(self.__height))

    def __repr__(self):
        """
        returns string
        representation of rectangle
        """
        class_name = (type(self).__name__)
        s = "{}({}, {})".format(class_name, self.__width, self.__height)
        return s

    def __del__(self):
        """
        deletes
        instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
