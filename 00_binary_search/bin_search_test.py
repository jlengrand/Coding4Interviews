"""
Unit tests for the binary search algorithm
@jlengrand
2013/07
"""
from bin_search import bin_search

import unittest


class test_bin_search(unittest.TestCase):

    def setUp(self):
        self.arr1 = [1, 2, 3, 4, 5]
        self.s1 = 3
        self.res1 = None

        self.arr2 = None
        self.arr3 = []
        self.arr4 = 345

    def test_bin_search(self):
        # Test None input
        res = bin_search(self.arr2, self.s1)
        self.assertEqual(res, self.res1)

        # Test empty table
        res = bin_search(self.arr3, self.s1)
        self.assertEqual(res, self.res1)

        # Test strange input
        res = bin_search(self.arr4, self.s1)
        self.assertEqual(res, self.res1)

        # Test simple table
        res = bin_search(self.arr1, self.s1)
        self.assertEqual(res, self.res1)



if __name__ == '__main__':
    unittest.main()
