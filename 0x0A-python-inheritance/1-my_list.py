#!/usr/bin/python3
"""Defines a class that inherit from MyList"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
