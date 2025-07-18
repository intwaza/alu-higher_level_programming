#!/usr/bin/python3
"""
Module that defines a function to convert a class instance to a dictionary
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure 

    Args:
        obj: An instance of a Class

    Returns:
        dict: Dictionary description of the object
    """
    return obj.__dict__
