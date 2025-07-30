#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test list with single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_positive_integers(self):
        """Test list with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 20, 30]), 30)

    def test_negative_integers(self):
        """Test list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20]), -5)
        self.assertEqual(max_integer([-100, -50, -25]), -25)

    def test_mixed_integers(self):
        """Test list with mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 5, -10, 3]), 5)
        self.assertEqual(max_integer([10, -20, 30, -5]), 30)
        self.assertEqual(max_integer([-5, -10, 2, -1]), 2)

    def test_max_at_beginning(self):
        """Test when maximum is at the beginning"""
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)
        self.assertEqual(max_integer([100, 50, 25]), 100)

    def test_max_at_end(self):
        """Test when maximum is at the end"""
        self.assertEqual(max_integer([1, 2, 5, 10]), 10)
        self.assertEqual(max_integer([25, 50, 100]), 100)

    def test_max_in_middle(self):
        """Test when maximum is in the middle"""
        self.assertEqual(max_integer([1, 10, 5]), 10)
        self.assertEqual(max_integer([3, 1, 15, 2, 8]), 15)

    def test_duplicate_max_values(self):
        """Test list with duplicate maximum values"""
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)
        self.assertEqual(max_integer([10, 10, 5, 10]), 10)

    def test_all_same_elements(self):
        """Test list where all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-3, -3, -3]), -3)

    def test_two_elements(self):
        """Test list with exactly two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([0, 5]), 5)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([2147483647, 2147483646]), 2147483647)

    def test_zero_included(self):
        """Test lists that include zero"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, 0, -2]), 0)
        self.assertEqual(max_integer([0, -1, -5]), 0)

    def test_long_list(self):
        """Test with longer lists"""
        long_list = list(range(1, 101))  # [1, 2, 3, ..., 100]
        self.assertEqual(max_integer(long_list), 100)
        
        reverse_list = list(range(100, 0, -1))  # [100, 99, 98, ..., 1]
        self.assertEqual(max_integer(reverse_list), 100)

    def test_random_order(self):
        """Test with randomly ordered elements"""
        self.assertEqual(max_integer([42, 17, 89, 3, 56]), 89)
        self.assertEqual(max_integer([123, 456, 789, 12, 34]), 789)


if __name__ == '__main__':
    unittest.main()
