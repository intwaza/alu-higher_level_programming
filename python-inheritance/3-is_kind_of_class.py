#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function to check if an object is an instance of or i
nherits from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of or inherits from a_class"""
    return isinstance(obj, a_class)
