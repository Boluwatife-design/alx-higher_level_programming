#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set(my_list)
    total = 0
    for x in unique_int:
        total += x
    return total
