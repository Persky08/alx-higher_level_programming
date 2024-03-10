#!/usr/bin/python3
""" a function that defines a square """


class Square:
    """ a class that defines a square"""
    def __int__(self, size=0):
        '''
        initializing a new square
        Args:
            size: the size of the square
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.__size = size
