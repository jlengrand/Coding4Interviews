"""
Unit tests for the Hash Map table implementation
@jlengrand
2013/11
"""

from hm import HashMap

import unittest


class test_hash_map(unittest.TestCase):

	def test_size(self):
	
		hm = HashMap()
		self.assertEqual(hm.size(), 0)

if __name__ == "__main__":
	unittest.main()
