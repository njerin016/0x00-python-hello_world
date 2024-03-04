#!/usr/bin/python3
"""
Class that defines a square
"""


class Square:
    """
    Attributes:
    Size: size of a square which is initialized as 0
    Methods (None):
    It has no methods
    """
    def __init__(self, size=0):
        """
        Constructor initializing a new instance of the square class
        Args:
        size: size of te square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
