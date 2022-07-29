#!/usr/bin/python3
"""Module: base_geometry (raising Exceptions and validating values)"""


class BaseGeometry:
    """create class BaseGeometry"""

    def area(self):
        """public instance that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
