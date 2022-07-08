#!/usr/bin/python3
def uppercase(str):
    for c in str:
        character = ord(c)
        if 97 <= character <= 122:
            charcter -= 32
        print("{:c}".format(character), end='')
    print()
