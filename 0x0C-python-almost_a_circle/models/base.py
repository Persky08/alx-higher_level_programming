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
        """
        initializing the class
        """
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        defines sharing data representation
        list_dictinaries:
                        dictionary
        """
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    
    @staticmethod
    def save_to_file(cls, list_objs):
        """
        Json string representation of a list to a file

        Args:
            list_objs(list): a list of instance

        Returns:
                None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, mode="w", encoding="utf-s") as file:
            file.write(json_string)
