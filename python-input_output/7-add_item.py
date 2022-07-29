#!/usr/bin/python3
"""Function that writes object to txt file using JSON representation"""
import json
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

my_list = []
if path.isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")
save_to_json_file(my_list + sys.argv[1:], "add_item.json")
