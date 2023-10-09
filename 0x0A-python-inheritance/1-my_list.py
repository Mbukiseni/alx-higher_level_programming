#!/usr/bin/python3
"""MyList inherits from list class"""

class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
