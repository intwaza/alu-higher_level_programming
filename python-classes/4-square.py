#!/usr/bin/python3
"""Module 4-square
Defines a Square class with getter and setter for size.
"""


class Square:
    """Represents a square with a private size attribute, area method, and property methods."""

    def __init__(self, size=0):
        """Initialize the square with a size value using the setter."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
