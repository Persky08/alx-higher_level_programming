#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for c in a_dictionary:
        new_dict[c] = a_dictionary[c] * 2
    return new_dict
