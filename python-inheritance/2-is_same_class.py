#!/usr/bin/python3
"""
Module 2-is_same_class

Checks if an object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
