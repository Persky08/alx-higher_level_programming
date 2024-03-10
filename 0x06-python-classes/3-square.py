#!/usr/bin/python3
'''
a program that creates a square
'''


class Square:

    """ defining a class object"""
    def __init__(self, size=0):
        """ initiliazing the square class
        Args:
            size: size of the square
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """a function that returns the area of a square"""
        return self.size * self.size
