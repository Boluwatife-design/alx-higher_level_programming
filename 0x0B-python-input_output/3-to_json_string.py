#!/usr/bin/python3
"""Defines a function that returns the JSON rep of a string"""


def to_json_string(my_obj):
    """Return the JSON representation of an object"""
    return json.dumps(my_obj)
