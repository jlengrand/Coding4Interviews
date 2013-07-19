"""
Unit tests for the binary search tree data structure
@jlengrand
2013/07
"""

from bst import BinarySearchTree
from bst import BinarySearchIterator

import unittest


class test_binary_search_tree(unittest.TestCase):

    def test_add(self):

        bst = BinarySearchTree()
        self.assertEqual(bst.size, 0)

        node_val1 = 6
        bst.add(node_val1)

        self.assertEqual(bst.size, 1)

        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
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
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)
        self.assertEqual(bst.size, 4)

        node = bst.root_node  # we have 6
        self.assertEqual(node.value, node_val1)
        self.assertTrue(node.has_left_child())
        self.assertEqual(node.left_child.value, node_val2)
        self.assertTrue(node.has_right_child())
        self.assertEqual(node.right_child.value, node_val3)

        node = node.left_child  # we have 4 now
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
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)
        self.assertEqual(bst.size, 4)

        self.assertEqual(bst.max(), node_val4)

    def test_min(self):

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        bst = BinarySearchTree()

        self.assertEqual(bst.min(), None)

        node_val1 = 6
        bst.add(node_val1)
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)
        self.assertEqual(bst.size, 4)

        self.assertEqual(bst.min(), node_val2)

    def test_is_search_node(self):
        bst = BinarySearchTree()

        self.assertEqual(bst.min(), None)

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        node_val1 = 6
        bst.add(node_val1)
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)

        self.assertTrue(BinarySearchTree.is_search_node(bst.root_node))
        self.assertTrue(BinarySearchTree.is_search_node(bst.root_node.left_child))
        self.assertTrue(BinarySearchTree.is_search_node(bst.root_node.right_child))
        self.assertTrue(BinarySearchTree.is_search_node(None))

    def test_is_search_tree(self):
        # No assertion here, I just want a beautifully designed tree.
        bst = BinarySearchTree()

        self.assertEqual(bst.min(), None)

        node_val1 = 6
        bst.add(node_val1)
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        self.assertTrue(BinarySearchTree.is_search_tree(bst.root_node))

        #    6
        #   / \
        #  8   10
        #       \
        #        16
        bst.root_node.left_child.value = 8
        self.assertEqual(bst.root_node.left_child.value, 8)
        self.assertFalse(BinarySearchTree.is_search_tree(bst.root_node))

        #    12
        #   / \
        #  4   10
        #       \
        #        16
        bst.root_node.left_child.value = 4
        self.assertEqual(bst.root_node.left_child.value, 4)
        bst.root_node.value = 12
        self.assertEqual(bst.root_node.value, 12)
        self.assertFalse(BinarySearchTree.is_search_tree(bst.root_node))

        #    6
        #   / \
        #  4   20
        #       \
        #        16
        bst.root_node.left_child.value = 6
        self.assertEqual(bst.root_node.left_child.value, 6)
        bst.root_node.right_child.value = 20
        self.assertEqual(bst.root_node.right_child.value, 20)
        self.assertFalse(BinarySearchTree.is_search_tree(bst.root_node))

    def test_print_node(self):
        bst = BinarySearchTree()

        self.assertEqual(bst.min(), None)

        node_val1 = 6
        bst.add(node_val1)
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        #self.assertEqual(bst.__str__(), "4 6 10")

        self.assertEqual(bst.root_node.__str__(), "4 6 10")
        self.assertEqual(bst.root_node.right_child.__str__(), "10 16")
        self.assertEqual(bst.root_node.right_child.right_child.__str__(), "16")

    def test_print_tree(self):
        bst = BinarySearchTree()

        self.assertEqual(bst.min(), None)

        node_val1 = 6
        bst.add(node_val1)
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        self.assertEqual(bst.__str__(), "4 6 10 16")

    def test_iterator(self):

        bst = BinarySearchTree()

        self.assertEqual(bst.min(), None)

        node_val1 = 6
        bst.add(node_val1)
        node_val2 = 4
        bst.add(node_val2)
        node_val3 = 10
        bst.add(node_val3)
        node_val4 = 16
        bst.add(node_val4)

        #    6
        #   / \
        #  4   10
        #       \
        #        16

        ite = BinarySearchIterator(bst)
        self.assertEquals(ite.tree, bst)
        print ite.next()
        print ite.next()
        print ite.next()
        print ite.next()



if __name__ == '__main__':
    unittest.main()
