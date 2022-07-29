#!/usr/bin/python3
"""Module: Task 10- square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherit from task 9"""
    def __init__(self, size):
        """initialize"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """pass number through area method"""
        return self.__size ** 2
