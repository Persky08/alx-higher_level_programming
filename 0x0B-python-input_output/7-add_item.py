#!/usr/bin/python3
"""
A module to load, add and save to python objects
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        # open the existing file
        old_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # create an empty file when file doesn't exist
        old_list = []

    # Extract new command line arguments
    new_file = sys.argv[1:]

    # Add new file to old list to create a new list
    new_list = old_list + new_file
    # save file to add_item.json
    save_to_json_file(new_list, "add_item.json")
