#!/usr/bin/python3
"""
Module 0-lookup
A function that returns the list of available attributes and methods.
"""


def lookup(obj):
    """Return the list of available attributes and methods of obj."""
    return dir(obj)
