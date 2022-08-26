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
        return ('[Square] ({d}) {d}/{d} - {d}'\
                .format(self.id, self.x, self.y, self.width))

