#!/usr/bin/python3
class Square:
    """ 
    Class that defines a square
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
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
