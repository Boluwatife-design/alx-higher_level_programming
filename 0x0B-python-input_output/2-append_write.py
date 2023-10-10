#!/usr/bin/python3
"""Defines a function that appends a string"""


def append_write(filename="", text=""):
    """appends a string and return the number of character added
    
    :filename(str):name of file to append to
    :text(str)str to append to
    """
    with open(filename, 'a', encoding=UTF-8) as f:
        return f.write(text)
