#!/usr/bin/python3
"""Task 6: Square area and position"""


class Square:
    """class that prints area of square and it's position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size equals value"""
        if (type(value)) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, size=0, position=(0, 0)):
        """Initialize"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Gets position"""
        return self.__position

        @position.setter
    def position(self, value):
        
        """position equals value"""
        
        if (value is not tuple) or len(value) != 2:
            """value not tuple or value out of index"""
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (type(value[0]) or type(value[1])) is not int:
            """value not int"""
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] < 0 or value[1] < 0:
            """negative value"""
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """Returns area"""
        return self.__size**2

    def my_print(self):
        """prints # """
        sz = self.__size
        psn = self.__position
        if sz == 0:
            print()
        if psn[1] >= 0:
            for i in range(sz):
                p = " "
                a = '#'
                print((p*psn[0])+(a*sz))
        else:
            for i in range(sz):
                p = "_"
                a = '#'
                print((p*psn[0])+(a*sz))
