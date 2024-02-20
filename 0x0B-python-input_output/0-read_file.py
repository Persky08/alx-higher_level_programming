#!/usr/bin/python3
"""
A read file module
"""


def read_file(filename=""):
    """
    A function that reads file and prints to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
