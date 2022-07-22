#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end= '')
    except (IndexError): 
        print(i)
        return (i)
    else:
        print(i)
        return (i)
