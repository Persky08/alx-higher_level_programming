#!/usr/bin/python3
"""
definis a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class to inherit from base
    """
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        self.check_integer("width", value)
        self.check_positive("width", value)
        self.__width = value

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        self.check_integer("height", value)
        self.check_positive("height", value)
        self.__height = value

    @property
    def x(self):
        print("Retrieving x")
        return self.__x

    @x.setter
    def x(self, value):
        self.check_integer("x", value)
        self.check_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        print("Retrieving y")
        return self.__x

    @y.setter
    def(self, value):
        self.check_integer("y", value)
        self.check_non_negative("y", value)
        self.__y = value

    def area(self):
        """
        returns area of a rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


    def check_integer(self, attribute_name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute_name))

    def check_positive(self, attribute_name, value):
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))

    def check_non_negative(self, attribute, value):
        if value < 0:
            raise ValueError("{} must be >= 0">format(attribute_name))
        
