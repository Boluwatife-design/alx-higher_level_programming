#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            for item in my_list:
                print(item, end="")
        except Exception as e:
            print(f"Error: {e}")
            break
    print("")
