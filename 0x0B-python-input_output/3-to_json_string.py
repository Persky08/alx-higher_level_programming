#!/usr/bin/python3
"""
A JSON representation module
"""


import json


def to_json_string(my_obj):
    """
    from_json_string: a function to return the object(Python
    data structure) represented by a JSON string

    args:
    my_str: the object to be converted to JSON

    Returns:
    The JSON representation of the object
    """
    return json.dumps(my_obj)
