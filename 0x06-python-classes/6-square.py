#!/usr/bin/python3
""" a program that creates Square objects"""


class Square:
    """ creating a class object"""
    def __init__(self, size=0, position=(0, 0)):
        """ initializing the square object"""
        self.__size = size

    @property
    def size(self):
        """getter method for the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """a method to create the position of the square"""
        return self.__property

    @position.setter
    def position(self, value):
        """setter for the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ a method to calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)