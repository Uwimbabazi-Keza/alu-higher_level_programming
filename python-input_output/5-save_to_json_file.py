#!/usr/bin/python3
"""Function that saves object to txt file
using JSON representation"""


import json
"""ïmports json module"""


def save_to_json_file(my_obj, filename):
    """writes object to txt file"""
    with open(filename, 'w', encoding='utf-8') as f:
        o = json.dumps(my_obj)
        return f.write(o)
