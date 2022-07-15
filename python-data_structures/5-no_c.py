#!/usr/bin/env python3
def no_c(my_string):
    new_str = list(my_string)
    i=0
    for i in range(len(new_str)):
        if new_str[i] == 'c':
            new_str.remove('c')
        elif new_str[i] == 'C':
            new_str.remove('C')
        else:
            break
    s = " "
    return (s.join(new_str))
