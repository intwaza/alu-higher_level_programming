#!/usr/bin/python3
"""
Base module for the project
Contains the Base class that will serve as the foundation for other classes
"""

import json


class Base:
    """
    Base class to manage id attribute in all future classes

    Attributes:
        __nb_objects (int): Private class attribute to count objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries to convert

        Returns:
            str: JSON string representation, or "[]" if None/empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file

        Args:
            list_objs (list): List of instances that inherit from Base
                             (e.g., Rectangle or Square instances)
        """
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return list of dictionaries from JSON string representation

        Args:
            json_string (str): String representing a list of dictionaries

        Returns:
            list: List of dictionaries, or empty list if None/empty
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set

        Args:
            **dictionary: Dictionary of attributes to set

        Returns:
            Base: Instance of the class with attributes set
        """
        # Create a dummy instance with mandatory attributes
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # width, height
        elif cls.__name__ == "Square":
            dummy = cls(1)  # size
        else:
            dummy = cls()

        # Update the dummy instance with real values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from file

        Returns:
            list: List of instances of the current class
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()

            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**dict_obj) for dict_obj in list_dicts]

        except FileNotFoundError:
            return []
