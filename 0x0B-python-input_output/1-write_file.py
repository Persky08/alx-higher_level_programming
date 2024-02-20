#!/usr/bin/python3
"""
A write file module
"""


def write_file(filename="", text=""):
    """
    A function to write to a text
    """
    with open(filename, mode='w', encoding='utf-8') as File:
        return File.write(text)
