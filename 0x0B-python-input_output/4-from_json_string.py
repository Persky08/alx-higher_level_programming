#!/usr/bin/python3
"""
A function that returns a Python data structure represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    from_json_string: a function that returns the Python
    data structure represented by JSON string

    args:
    my_str: The JSON string

    Returns:
    Python data structure
    """
    return json.loads(my_str)
