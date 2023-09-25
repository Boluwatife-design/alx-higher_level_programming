#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_count += 1
        except(TypeError, IndexError):
            continue
    print("")
    return print_count
