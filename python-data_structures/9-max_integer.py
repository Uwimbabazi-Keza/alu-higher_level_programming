#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    if my_list:
        for i in my_list:
            if i >= maximum:
                maximum = i
        return maximum
    else:
        return None
