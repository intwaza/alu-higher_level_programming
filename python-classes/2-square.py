#!/usr/bin/python3
"""Module 2-square
Defines a Square class with size validation.
"""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size=0):
        """Initialize the square and validate size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
