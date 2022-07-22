#!/usr/bin/python3
class Square:
    """Square"""
    def __init__(self, size=0):
        """size"""
        self.size = size


    def size(self):
        """size"""
        return (self.__size)

    def size(self, value):
        """attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area"""
        return (self.__size * self.__size)

    def my_print(self):
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
