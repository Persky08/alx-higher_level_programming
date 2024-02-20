#!/usr/bin/python3
"""
A function that writes an object to a file, using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    save a python data structure as a file using json representation

    args:
        my_obj: The python object to be written
        filename: name of the file to write the json to

    Returns:
        none
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dumps(my_obj, my_file, indent=2)
