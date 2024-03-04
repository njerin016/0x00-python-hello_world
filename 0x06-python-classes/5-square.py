#!/usr/bin/python3
"""
A class that defines a square
"""


class Square:
    """
    Attribute:
    Size: the size of the square
    """
    def __init__(self, size=0):
        """
        Constructor that initializes an instance of the square class
        Args:
        size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """
        getter method: gets the current size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter method: sets a value to be the size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(size):
        """
        returns the area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
