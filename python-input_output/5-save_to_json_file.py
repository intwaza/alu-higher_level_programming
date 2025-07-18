#!/usr/bin/python3
"""
Module that defines a function to save an object to a file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    
    Args:
        my_obj: The object to save to the file
        filename (str): The name of the file to save to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
