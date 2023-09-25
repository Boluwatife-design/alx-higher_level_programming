#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError):
            result = 0
            if isinstance(my_list_1[i], (str, bool)) or isinstance(my_list_2[i], (str, bool)):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            else:
                print("out of range")
        finally:
            new_list.append(result)

    return new_list
