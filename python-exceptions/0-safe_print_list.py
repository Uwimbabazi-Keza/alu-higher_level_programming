#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list = my_list[:x]
        print(*my_list, sep = '')
    except (IndexError):
        return None
    else:
        return(x)
