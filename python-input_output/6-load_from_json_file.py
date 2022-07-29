#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""


import json
"""imports json module"""


def load_from_json_file(filename):
    """converts object from
    json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
