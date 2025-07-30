#!/usr/bin/python3
"""
Module that contains text_indentation function.
This module provides a function to print text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? :
    Args:
        text: string to be processed and printed
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    current_line = ""
    for char in text:
        current_line += char
        if char in '.?:':
            # Strip leading and trailing spaces from current line and print
            print(current_line.strip())
            # Print one empty line 
            print()
            # Reset current line
            current_line = ""
    # If there's remaining text, print it stripped
    if current_line.strip():
        print(current_line.strip())
