#!/usr/bin/python3
"""Add all arguments to a Python list and save to a JSON file."""
import sys
from json import dump, load
from os.path import exists

def load_from_json_file(filename):
    if exists(filename):
        with open(filename, 'r') as f:
            return load(f)
    return []

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        dump(my_obj, f)

if __name__ == "__main__":
    # Try to load existing data or create an empty list
    items = load_from_json_file("add_item.json")
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")

