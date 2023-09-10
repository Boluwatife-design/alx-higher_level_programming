#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence) if sentence else 0
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
