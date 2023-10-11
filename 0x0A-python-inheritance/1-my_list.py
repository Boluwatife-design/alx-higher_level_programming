#!/usr/bin/python3
"""Defines a class that inherit from my list"""


class MyList(list):
    """class that inherit from my list"""
    
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
