#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """using with statemnt for exception handling"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
