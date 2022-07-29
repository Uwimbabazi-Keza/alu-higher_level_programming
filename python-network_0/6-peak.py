#!/usr/bin/python3
"""Module: Peak"""


def find_peak(list_of_integers):
    """Finds a peak in a disorgainized list"""
     if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    x = len(list_of_integers) - 1
    l = 0
    int_list = list_of_integers
    while x > l:
        h = (x + l) // 2
        if my_list[h] <= my_list[h + 1]:
            l = h + 1
        elif my_list[h] <= my_list[h - 1]:
            x = h - 1
        elif my_list[h] >= my_list[h + 1] and my_list[h]\
                >= my_list[h - 1]:
            return my_list[h]
    return my_list[l]
