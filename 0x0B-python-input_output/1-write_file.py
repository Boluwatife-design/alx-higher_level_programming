#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    :filename(str):name of file to write
    :text(str):text to write to the file
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
