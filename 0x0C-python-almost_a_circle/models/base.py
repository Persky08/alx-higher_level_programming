#!/usr/bin/python3
"""
defines a class called base
"""
import json
import csv

class Base:
    """
    creating a class called base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
