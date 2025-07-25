#!/usr/bin/python3
"""
Module that defines a function to append a string to a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
