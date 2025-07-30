#!/usr/bin/python3
"""
Module that contains say_my_name function.
This module provides a function to print a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.
    
    Args:
        first_name: string representing the first name
        last_name: string representing the last name (defaults to empty string)
    
    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
