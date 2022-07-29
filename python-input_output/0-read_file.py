#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """using with statemnt for exception handling"""
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()
