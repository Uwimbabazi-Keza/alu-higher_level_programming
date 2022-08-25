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
        """Positive int test"""
        self.assertEqual(max_integer([5, 2, 10, 4]), 10)

    def negative_int_test(self):
        """Negative int test"""
        self.assertEqual(max_integer([-9, -2, -10, -4]), -2)

    def empty_list(self):
        """Empty list"""
        self.assertRaises(max_integer([]), None)

    def middle_test(self):
        """"middle test"""
        self.assertEqual(max_integer([2, 3, 8, 4, 5]), 8)

    def one_case(self):
        """"One case"""
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
