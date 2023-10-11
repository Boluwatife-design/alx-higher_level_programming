#!/usr/bin/python3
"""Defines a function that returns the list of available attribute"""

def lookup(obj):
    """returns a list object"""
    return dir(obj)
