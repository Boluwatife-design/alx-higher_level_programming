#!/usr/bin/python3
"""Defines a function that appends a file"""


def append_write(filename="", text=""):
    """appends a string to a file
    
    :filename(str):name of file to append to
    :text(str):str to append to file
    :Returns: number of character added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
