#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for new, c in enumerate(new_list):
        if c == search:
            new_list[new] = replace
    return new_list
