#!/usr/bin/python3
"""class Student defines student"""


class Student:
    """create class student"""

    def __init__(self, first_name, last_name, age):
        """initializate atrributes
        first_name:
        last_name:
        age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves dictionary of student"""
        return self.__dict__
