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

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dictionary
        rep of Square
        """
        dc = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

        return dc
