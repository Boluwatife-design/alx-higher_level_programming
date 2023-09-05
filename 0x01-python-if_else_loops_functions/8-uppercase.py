#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord(l) >= 65 and ord(l) <= 90:
            print("{}".format(l), end=" ")
