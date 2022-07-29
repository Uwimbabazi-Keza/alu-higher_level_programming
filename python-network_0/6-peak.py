#!/usr/bin/python3
"""Module: Peak"""


def find_peak(list_of_integers):
    """Finds a peak in a disorgainized list"""
     if len(list_of_integers) % 2 == 0:
        mid = (len(list_of_integers) // 2) - 1
    else:
        mid = len(list_of_integers) // 2

    p = list_of_integers[mid]

    if len(list_of_integers) <= 2:
        return max(list_of_integers)
    elif list_of_integers[mid - 1] <= \
            p and p >= \
            list_of_integers[mid + 1]:
        return p
    elif p < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
