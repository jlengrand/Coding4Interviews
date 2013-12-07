"""
Unit Tests for the Linked Lists implementations
@jlengrand
2013/12
"""

from ll import SingleListItem

import unittest

class test_single_linked_list_item(unittest.TestCase):

    def test_item(self):

        a = 12
        t = SingleListItem(12, None)

        self.assertEqual(a, t.value)

if __name__ == "__main__":
    unittest.main()