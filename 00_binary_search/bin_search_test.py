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
        self.res1 = False

        self.arr2 = None
        self.arr3 = []
        self.arr4 = 345

        self.arr5 = [3]
        self.s51 = 1
        self.res51 = False
        self.s52 = 3
        self.res52 = True

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

        # Testing length1 array
        res = bin_search(self.arr5, self.s51)
        self.assertEqual(res, self.res51)

        res = bin_search(self.arr5, self.s52)
        self.assertEqual(res, self.res52)


if __name__ == '__main__':
    unittest.main()
