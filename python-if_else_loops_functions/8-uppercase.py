#!/usr/bin/python3
def uppercase(str):
    for c in str:
        temp = ord(c)
        if ord(c) >= 97 and ord(c) <= 122:
            ord(c) -= 32
        print("{:c}".format(ord(c)), end='')
    print()