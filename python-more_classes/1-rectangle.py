#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class with private width and height attributes,
including getters and setters with validation.
"""


class Rectangle:
    """Defines a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
