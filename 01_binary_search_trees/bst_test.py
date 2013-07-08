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

        node_val1 = 6
        bst.add(node_val1)

        self.assertEqual(bst.size, 1)

        node_val2= 4
        bst.add(node_val2)
        node_val3= 10
        bst.add(node_val3)
        node_val4= 16
        bst.add(node_val4)
        self.assertEqual(bst.size, 4)

    def test_has_children(self):

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        bst = BinarySearchTree()
        node_val1 = 6
        bst.add(node_val1)
        node_val2= 4
        bst.add(node_val2)
        node_val3= 10
        bst.add(node_val3)
        node_val4= 16
        bst.add(node_val4)
        self.assertEqual(bst.size, 4)

        node = bst.root_node  # we have 6
        self.assertEqual(node.value, node_val1)
        self.assertTrue(node.has_left_child())
        self.assertEqual(node.left_child.value, node_val2)
        self.assertTrue(node.has_right_child())
        self.assertEqual(node.right_child.value, node_val3)

        node = node.left_child # we have 4 now
        self.assertFalse(node.has_left_child())
        self.assertFalse(node.has_right_child())


    def test_max(self):

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        bst = BinarySearchTree()

        self.assertEqual(bst.max(), None)

        node_val1 = 6
        bst.add(node_val1)
        node_val2= 4
        bst.add(node_val2)
        node_val3= 10
        bst.add(node_val3)
        node_val4= 16
        bst.add(node_val4)
        self.assertEqual(bst.size, 4)

        self.assertEqual(bst.max(), node_val4)

if __name__ == '__main__':
    unittest.main()