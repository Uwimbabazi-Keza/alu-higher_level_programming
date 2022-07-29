#!/usr/bin/python3
"""Function that writes object to txt file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to txt file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dumps(my_obj)
