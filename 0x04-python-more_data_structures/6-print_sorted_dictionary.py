#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = list(a-dictionary.keys())
    list_keys.sort()
    for key in list_keys:
        print("{}:{}".format(keys, a_dictionary[key]))
