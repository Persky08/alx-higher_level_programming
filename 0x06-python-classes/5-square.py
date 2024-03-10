#!/usr/bin/python3
""" A program prints a square"""


class Square:
    """ A square object"""
    def __init__(self, size=0):
        """initializing square object
        Args:
            Size: The size of the objece
        """
        self.__size = size

    @property
    def size(self):
        """getter method for size attribute"""
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
        """ a method that calculates the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """a method that prints #"""
        print("#")
        if size == 0:
            print()
