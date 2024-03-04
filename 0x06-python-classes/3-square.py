#!usr/bin/python3
"""
A class that defines a square
"""
class Square:
    """
    Attributes:
    Size: size of a square which is initialized as 0
    """
    def __init__(self, size = 0):
        """
        Constructor initializing a new instance of the sqare class
        Args:
        size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Method:
        returns the area of the square
        """
        return (self.__size * self.__size)
