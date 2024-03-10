#!/usr/bin/python3
""" a program that access and update private attributes"""


class Square:
    """ creating a square object"""

    def __init__(self, size=0):
        '''
        a function that initialize square object
        '''
        self.__size = size

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the area of the square"""
        return self.__size * self.__size
