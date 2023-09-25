#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """print first element of a list
    :param my_list: The list to print integers from.
    :param x: The number of integers to print.
    :return: The count of integers successfully printed.
    """
    print_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_count += 1
        except(TypeError, ValueError):
            continue
    print("")
    return print_count
