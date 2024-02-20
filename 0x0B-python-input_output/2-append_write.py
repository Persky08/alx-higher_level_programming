#!/usr/bin/python3
"""
A module to append to file
"""


def append_write(filename="", text=""):
    """
    A function to append new text to an already existing file
    """
    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
