#!/usr/bin/python3
"""Module 7-rectangle
Defines a Rectangle class with customizable print symbol and instance tracking.
"""


class Rectangle:
    """Defines a rectangle with width, height, instance counting,
    and customizable print symbol for string representation."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle as a string using print_symbol.
        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Convert print_symbol to string (in case it's not)
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string that can be used by eval()."""
        return (f"{self.__class__.__name__}"
                f"({self.__width}, {self.__height})")


    def __del__(self):
        """Print message when instance is deleted and decrement instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
