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
        self.res1 = True

        self.res2 = False
        self.arr2 = None
        self.arr3 = []
        self.arr4 = 345

        self.arr5 = [3]
        self.s51 = 1
        self.res51 = False
        self.s52 = 3
        self.res52 = True


        self.arr6 = [1, 3, 9, 14, 22]
        self.s61 = 22
        self.s62 = 3
        self.s63 = 16
        self.res61 = True
        self.res62 = True
        self.res63 = False

        self.arr7 = [1, 3, 9, 14, 22, 25]
        self.s71 = 22
        self.res71 = True
        self.s72 = 3
        self.res72 = True
        self.s73 = 58
        self.res73 = False

    def test_bin_search(self):
        # Test None input
        res = bin_search(self.arr2, self.s1)
        self.assertEqual(res, self.res2)

        # Test empty table
        res = bin_search(self.arr3, self.s1)
        self.assertEqual(res, self.res2)

        # Test strange input
        res = bin_search(self.arr4, self.s1)
        self.assertEqual(res, self.res2)

        # Testing length1 array
        res = bin_search(self.arr5, self.s51)
        self.assertEqual(res, self.res51)

        res = bin_search(self.arr5, self.s52)
        self.assertEqual(res, self.res52)

        # longer array easy
        res = bin_search(self.arr1, self.s1)
        self.assertEqual(res, self.res1)

        # longer array has to search / odd
        res = bin_search(self.arr6, self.s61)
        self.assertEqual(res, self.res61)

        res = bin_search(self.arr6, self.s62)
        self.assertEqual(res, self.res62)

        res = bin_search(self.arr6, self.s63)
        self.assertEqual(res, self.res63)

        # longer array has to search / even
        res = bin_search(self.arr7, self.s71)
        self.assertEqual(res, self.res71)

        res = bin_search(self.arr7, self.s72)
        self.assertEqual(res, self.res72)

        res = bin_search(self.arr7, self.s73)
        self.assertEqual(res, self.res73)

if __name__ == '__main__':
    unittest.main()
