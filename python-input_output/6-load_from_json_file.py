#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""


import json
"""ïmports json module"""


def save_to_json_file(my_obj, filename):
    """converts object from json file to pyobject"""
    with open(filename, 'r', encoding='utf-8') as f:
        o = json.loads(my_obj)
        return f.write(o)
