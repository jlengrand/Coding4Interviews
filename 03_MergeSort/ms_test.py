"""
Unit Tests for the MergeSort implementation
@jlengrand
2013/12
"""

from ms import TableSorter

import unittest

class test_table_sorter(unittest.TestCase):

    def test_merge(self):
        table = [1, 2]
        t_1 = [1]
        t_2 = [2]

        sorter = TableSorter()
        self.assertEqual(table, sorter._merge(t_1, t_2))

        t_1 = [2]
        t_2 = [1]
        self.assertEqual(table, sorter._merge(t_1, t_2))

        table = [1, 2, 3, 5]
        t_1 = [2, 5]
        t_2 = [1, 3]
        self.assertEqual(table, sorter._merge(t_1, t_2))

        t_1 = [3, 5]
        t_2 = [1, 2]
        self.assertEqual(table, sorter._merge(t_1, t_2))

    def test_mergeSort(self):

        table = []
        sorter = TableSorter()
        self.assertEqual(None, sorter.mergeSort(table))

        table = [1]
        self.assertEqual(table, sorter.mergeSort(table))

        table = [1, 2]
        self.assertEqual(table, sorter.mergeSort(table))


if __name__ == "__main__":
    unittest.main()
