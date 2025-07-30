#!/usr/bin/python3
"""
Square module for the project
Contains the Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute (returns width since width == height)"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return string representation of the Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Update Square attributes using positional or keyword arguments
        """
        if args:
            # If args exist and not empty, use positional arguments
            attributes = ['id', 'size', 'x', 'y']

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
        Return the dictionary representation of the Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
