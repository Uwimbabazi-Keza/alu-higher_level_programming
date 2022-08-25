#!/usr/bin/python3
"""
Module running unittest on a function returning max int
"""


import unittest
"""
import unittest module
"""

max_integer = __import__('6-max_integer').max_integer

class max_int_tests(unittest.TestCase):
    """
    tests
    """
    def max_integer(self):
        self.assertEqual(max_integer([5, 2, 10, 4]), 10)
        self.assertEqual(max_integer([9, 2, -10, 4]), 9)
        self.assertRaises(max_integer([5, 2, '10', 4]), (TypeError))
        self.assertRaises(max_integer([5, 2.3, 10.8, 4]), (TypeError))
        self.assertRaises(max_integer([]), None))
