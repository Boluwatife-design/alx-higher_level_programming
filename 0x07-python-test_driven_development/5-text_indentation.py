#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

        :text (string): The text to print.
    raise:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = 0
    while n < len(text) and text[n] == ' ':
        n += 1

    while n < len(text):
        print(text[n], end="")
        if text[n] == "\n" or text[n] in ".?:":
            if text[n] in ".?:":
                print("\n")
            n += 1
            while n < len(text) and text[n] == ' ':
                n += 1
            continue
        n += 1
