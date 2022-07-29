#!/usr/bin/python3
"""Function that appends a string at end of text file
and returns char count added"""


def append_write(filename="", text=""):
    """Appends string to end of txt file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
