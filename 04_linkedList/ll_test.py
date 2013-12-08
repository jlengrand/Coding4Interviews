"""
Unit Tests for the Linked Lists implementations
@jlengrand
2013/12
"""

from ll import SingleListItem
from ll import SingleLinkedList

import unittest

class test_single_linked_list_item(unittest.TestCase):

    def test_item(self):

        a = 12
        t = SingleListItem(12)

        self.assertEqual(a, t.value)

	def test_has_next(self):
		a = 12
        t = SingleListItem(12)

        self.assertEqual(False, t.has_next())

        b = SingleListItem(13, t)
        self.assertEqual(True, b.has_next())


class test_single_linked_list(unittest.TestCase):

    def test_add(self):
        a = 12
        sl = SingleLinkedList()

        sl.add(a)
        self.assertEqual(1, len(sl))

        sl.add(a)
        self.assertEqual(2, len(sl))

    def test_delete_item(self):
        sl = SingleLinkedList()

        sl.add(1)
        sl.add(2)
        sl.add(3)
        self.assertEqual(3, len(sl))

        self.assertEqual(1, sl._root.value)

        self.assertRaises(Exception, lambda x : sl.delete_item(4))

        sl.delete_item()
        self.assertEqual(2, len(sl))
        self.assertEqual(2, sl._root.value)

        sl.add(4)
        sl.add(5)
        sl.add(6)

        sl.delete_item(len(sl) - 1)
        self.assertEqual("2, 3, 4, 5", sl.__str__())

        sl.delete_item(1)
        self.assertEqual("2, 4, 5", sl.__str__())

        sl.delete_item()
        self.assertEqual("4, 5", sl.__str__())

    def test_delete(self):
        sl = SingleLinkedList()

        sl.add(2)
        sl.add(1)
        sl.add(3)
        self.assertEqual(3, len(sl))

        self.assertEqual(2, sl._root.value)

        self.assertRaises(Exception, lambda x: sl.delete(4))

        sl.delete(1)
        self.assertEqual("2, 3", sl.__str__())

        sl.delete(2)
        self.assertEqual("3", sl.__str__())

        sl.delete(3)
        self.assertEqual("Empty List", sl.__str__())
        self.assertEqual(0, len(sl))

    def test_search(self):

        sl = SingleLinkedList()

        sl.add(2)
        sl.add(1)
        sl.add(3)
        self.assertEqual(3, len(sl))

        self.assertEqual(True, sl.search(2))
        self.assertEqual(True, sl.search(3))
        self.assertEqual(True, sl.search(1))

        self.assertEqual(False, sl.search("a"))
        self.assertEqual(False, sl.search(4))
        self.assertEqual(False, sl.search(12))

    def test_get(self):

        sl = SingleLinkedList()

        sl.add(2)
        sl.add(1)
        sl.add(3)
        sl.add(4)
        sl.add(5)
        sl.add(6)

        self.assertEqual(6, len(sl))

        self.assertEqual(2, sl.get(0))
        self.assertEqual(1, sl.get(1))
        self.assertEqual(3, sl.get(2))
        self.assertEqual(4, sl.get(3))
        self.assertEqual(5, sl.get(4))
        self.assertEqual(6, sl.get(5))

        self.assertRaises(Exception, lambda x: sl.get(14))

if __name__ == "__main__":
    unittest.main()
