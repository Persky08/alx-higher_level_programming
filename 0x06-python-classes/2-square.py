#!/usr/bin/python3
"""a program that defines a square class."""


class Square:
    """Square class body"""

    def __init__(self, size=0):
        """Square class contructor
        Args:
            size: The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
