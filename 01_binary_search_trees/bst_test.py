"""
Unit tests for the binary search tree data structure
@jlengrand
2013/07
"""

from bst import BinarySearchTree

import unittest


class test_binary_search_tree(unittest.TestCase):

    def test_add(self):

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)


if __name__ == '__main__':
    unittest.main()