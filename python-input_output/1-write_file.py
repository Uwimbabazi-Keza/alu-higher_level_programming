#!/usr/bin/python3
"""Function that writes a str to a text file
and returns char count"""


def write_file(filename="", text=""):
    """"writes string to text file"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
