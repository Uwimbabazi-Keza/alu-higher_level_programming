#!/usr/bin/python3
"""Module: My List class"""


class MyList(list):
    """class MyList inherits from list"""
    def print_sorted(self):
        """ascending order"""
        print(sorted(self))
