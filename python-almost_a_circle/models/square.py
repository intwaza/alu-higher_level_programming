#!/usr/bin/python3
"""
Square module for the project
Contains the Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle

    A Square is a special Rectangle where width and height are equal (size)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square

        Args:
            size (int): The size of the square (both width and height)
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): The id of the square. If None, auto-generated.
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

        Sets both width and height to the same value
        Uses Rectangle's width validation
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return string representation of the Square

        Returns:
            str: String in format '[Square] (<id>) <x>/<y> - <size>'
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Update Square attributes using positional or keyword arguments

        Args:
            *args: Variable number of positional arguments in order:
                1st argument: id attribute
                2nd argument: size attribute
                3rd argument: x attribute
                4th argument: y attribute
            **kwargs: Key-value pairs where keys are attribute names

        Note: **kwargs is skipped if *args exists and is not empty
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

        Returns:
            dict: Dictionary containing all Square attributes
                    (id, size, x, y)
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
