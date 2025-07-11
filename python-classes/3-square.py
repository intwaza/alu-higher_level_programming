#!/usr/bin/python3
"""Module 3-square
Defines a Square class with size validation and area method.
"""


class Square:
    """
    Represents a square with size validation and a method to compute area
    """

    def __init__(self, size=0):
        """Initialize the square and validate size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
