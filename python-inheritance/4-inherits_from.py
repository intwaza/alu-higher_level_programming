#!/usr/bin/python3
"""
Module 4-inherits_from

Defines a function to check if an object is an instance of a class
that inherits (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherits from a_class,
    otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
