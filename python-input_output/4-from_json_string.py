#!/usr/bin/python3
"""
Module that defines a function to convert a JSON string to an object
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): The JSON string to convert to a Python object

    Returns:
        object: Python data structure represented by the JSON string
    """
    return json.loads(my_str)
