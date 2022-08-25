#!/usr/bin/python3
"""
Module running unittest on a function returning max int
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    tests
    """
    def positive_int_test(self):
        self.assertEqual(max_integer([5, 2, 10, 4]), 10)

    def negative_int_test(self):
        self.assertEqual(max_integer([9, 2, -10, 4]), 9)

    def empty_list(self)
        self.assertRaises(max_integer([]), None)

if __name__== "__main__":
    if __name__ == '__main__':
    unittest.main()
