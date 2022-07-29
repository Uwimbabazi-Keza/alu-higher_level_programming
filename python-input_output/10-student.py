#!/usr/bin/python3
""""class Student defines student based on task 9"""


class Student:
    """Ïnitialize"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves student"""
        attrib = {}
        if attrs is not None and all(isinstance(keyy, str)
        for keyy in attrs):
            for i, j in self.__dict__.items():
                if i in attrs:
                    attrib[i] = j
            return attrib
        return self.__dict__
