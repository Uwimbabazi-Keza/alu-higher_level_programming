#!/usr/bin/python3
"""Module: function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True regardless of whether object is an instance
    of a class that directly or indirectly inherited from
    specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
