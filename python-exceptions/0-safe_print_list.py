#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        print(*new_list, sep = '')
        print(x)
    except:
        return None
