#!/usr/bin/python3
"""Module that defines MyList class inherited from list"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
