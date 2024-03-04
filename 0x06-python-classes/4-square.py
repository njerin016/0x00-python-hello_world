#!/usr/bin/python3
"""
A class that defines a square
"""


class Square:
    """
    Atrribute:
    Size: size of the square initialized as 0
    """
    def __init__(self, size=0):
        """
        Constructor initializing a new instance of the square class
        Args:
        size: size of the square
        """

    @property
    def size(self):
        """
        getter method: gets the current size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter method: sets a value to size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the area of the square
        """
        return (self.__size * self.__size)
