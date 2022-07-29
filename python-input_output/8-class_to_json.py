#!/usr/bin/python3
"""Returns dictionary description for JSON serialization"""


def class_to_json(obj):
    """Returns with simple data structure for JSON serialization"""
    return obj.__dict__
