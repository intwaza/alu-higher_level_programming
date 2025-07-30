#!/usr/bin/python3
"""
Module that contains print_square function.
This module provides a function to print a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.
    Args:
        size: integer representing the size length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    # Special case: float and < 0 should raise TypeError
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    # Check if size is an integer (excluding bool which is subclass of int)
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    # Check if size is negative
    if size < 0:
        raise ValueError("size must be >= 0")
    # Print the square
    for i in range(size):
        print("#" * size)
