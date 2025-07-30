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

    c = 0
    # Skip leading spaces
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            # Skip spaces after punctuation
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
