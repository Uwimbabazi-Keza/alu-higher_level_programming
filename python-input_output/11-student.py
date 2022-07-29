#!/usr/bin/python3
"""class Student that defines a student based on task 10"""


class Student:
    """Initialize"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """writes object to txt file"""
        attrib = {}
        if attrs is not None and all(isinstance(keyy, str) for keyy in attrs):
            for i, j in self.__dict__.items():
                if i in attrs:
                    attrib[i] = j
            return attrib
        return self.__dict__

    def reload_from_json(self, json):
        """writes object to txt file"""
        for i, j in json.items():
            self.__dict__[i] = j
