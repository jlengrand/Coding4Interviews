"""
Unit Tests for the MergeSort implementation
@jlengrand
2013/12
"""

from ms import TableSorter

import unittest

class test_table_sorter(unittest.TestCase):

    #TODO: Implement
    def test_mergeSort(self):

        table = [1]
        sorter = TableSorter()
        self.assertEqual(None, sorter.mergeSort(table))


if __name__ == "__main__":
    unittest.main()
