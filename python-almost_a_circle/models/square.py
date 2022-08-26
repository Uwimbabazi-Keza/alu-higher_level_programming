#!/usr/bin/python3
"""
Module contains class square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """sub class of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        s = '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        """returns size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
