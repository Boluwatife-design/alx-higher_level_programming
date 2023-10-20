#!/usr/bin/python3
"""Defines a function that adds a new attribute"""

def add_attribute(obj, att, value):
    """adds a new attribute to an object if it’s possible

    :obj: the object to add an attribute to
    :att: attribute to be added
    :value: the value of attribute
    Raises:
        TypeError exception
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
