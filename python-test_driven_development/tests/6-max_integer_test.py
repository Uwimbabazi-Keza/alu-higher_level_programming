#!/usr/bin/python3
"""
Module running unittest on a function returning max int
"""


import unittest
"""
import unittest module
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class max_int_tests(unittest.TestCase):
    def max_integer(self):
        self.assertEqual(max_integer([5, 2, 10, 4]), 10)
        self.assertEqual(max_integer([9, 2, -10, 4]), 9)
        self.assertRaises(max_integer([5, 2, '10', 4]), (TypeError))
        self.assertRaises(max_integer([5, 2.3, 10.8, 4]), (TypeError))
        self.assertRaises(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
