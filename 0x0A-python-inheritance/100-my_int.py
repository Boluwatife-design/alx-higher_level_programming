#!/usr/bin/python3
"""Defines a class that inherit from int"""

class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior"""
        return self.real == value
