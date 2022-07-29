#!/usr/bin/python3
"""Function that returns an object represented by a JSON str"""


import json


def from_json_string(my_str):
    """returns object"""
    return json.loads(my_str)
