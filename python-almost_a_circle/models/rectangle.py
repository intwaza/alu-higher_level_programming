#!/usr/bin/python3
"""
Rectangle module for the project
Contains the Rectangle class that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base

    Manages rectangle objects with width, height, x, y coordinates and id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle instance to stdout using the character '#'
        """
        # Print y empty lines for vertical positioning
        for _ in range(self.y):
            print()

        # Print the rectangle with x spaces for horizontal positioning
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return string representation of the Rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
            """
            Update Rectangle attributes using positional or keyword arguments
            """
            if args:
                # If args exist and not empty, use positional arguments
                attributes = ['id', 'width', 'height', 'x', 'y']

                for i, value in enumerate(args):
                    if i < len(attributes):
                        setattr(self, attributes[i], value)
            else:
                # If no args provided, use keyword arguments
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
