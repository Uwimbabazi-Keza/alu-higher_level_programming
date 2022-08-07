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
        if ((((len(value) != 2)) or ((type(value[0]) and type(value[1])) is not int)) or\
            ((value[0] and value[1]) < 0)):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value
    
    def area(self):
        return self.__size**2
    
    def my_print(self):
        sz = self.__size
        psn = self.__position
        if sz == 0:
            print()
        if psn[1] >= 0:
            for i in range(sz):
                p = ""
                a = '#'
                print((p*psn[0])+(a*sz))
        else: 
            for i in range(sz):
                p = "_"
                a = '#'
                print((p*psn[0])+(a*sz))
