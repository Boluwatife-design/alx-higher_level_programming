#!/usr/bin/python3
"""Defines a function that appends a string"""


def append_write(filename="", text=""):
    """appends a string and return the number of character added
    
    :filename(str):name of file to append to
    :text(str)str to append to file
    Return: number of character added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
