#!/usr/bin/python3
"""Module: Peak"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    l = len(list_of_integers)
    if l % 2 == 0:
        mid = (l // 2) - 1
    else:
        mid = (l // 2)

    if l <= 2:
        return max(list_of_integers)
    elif list_of_integers[mid - 1] <= list_of_integers[mid]\
            and list_of_integers[mid] >= \
            list_of_integers[mid + 1]:
        return list_of_integers[mid]

    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
