#!/usr/bin/python3
"""
Module that contains add_integer function.
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98
    
    Returns:
        int: the addition of a and b as an integer
    
    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
