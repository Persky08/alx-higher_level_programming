#!/usr/bin/python3
"""Contain function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from json file
    args:
        filename: The name of the file to be created
    """
    with open(filename) as my_file:
        return json.load(my_file)
