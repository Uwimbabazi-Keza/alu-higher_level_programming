#!/usr/bin/python3
"""Module: is_same_class"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class"""
    return type(obj) is a_class
