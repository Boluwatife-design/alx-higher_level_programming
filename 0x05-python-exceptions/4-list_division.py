#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            element1 = my_list_1[i] if i < len(my_list_1) else None
            element2 = my_list_2[i] if i < len(my_list_2) else None
            if element1 is None or element2 is None:
                raise IndexError("out of range")
            result = element1 / element2
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrongtype")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
