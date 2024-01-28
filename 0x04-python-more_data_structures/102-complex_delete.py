#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for word in list(a_dictionary):
        if a_dictionary[word] == value:
            del a_dictionary[word]
    return a_dictionary
