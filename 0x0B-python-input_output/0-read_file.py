#!/usr/bin/python3
"""
A program that reads from a file and print to stdout
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read())
