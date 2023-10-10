#!/usr/bin/python3
"""Defines function that read a text file"""


def read_file(filename=""):
    """Prints the UTF8 file to STDOUT"""
    with open('filename', encoding="UTF8") as f:
        print(f.read(), end="")
