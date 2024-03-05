#!/usr/bin/python3
"""
A class that defines a square
"""


class Square:
    """
    Attribute:
    Size: the size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor that initializes an instance of the square class
        Args:
        size: size of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        getter method: gets the current position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        setter method: sets a value to be the position of the square
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
