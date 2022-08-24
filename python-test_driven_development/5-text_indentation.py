#!/usr/bin/python3
"""
Module contains function that indents
text after special characters
"""


def text_indentation(text):
    """
    text indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    symbols = ['.', '?', ':']
    white_sp = True
    for t in text:
        if t == ' ' and white_sp:
            pass
        elif t in symbols:
            print("{}\n".format(t))
            white_sp = True
        else:
            print(t, end='')
            white_sp = False
