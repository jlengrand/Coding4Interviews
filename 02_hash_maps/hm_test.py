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

	def test__hash(self):
		hm = HashMap()
		
		value = "a"
		self.assertEqual(hm._hash(value), ord(value))
		
		value = "test"
		self.assertEqual(hm._hash(value), 502948)

		value = ""
		self.assertRaises(Exception, lambda x : hm._hash(value))

if __name__ == "__main__":
	unittest.main()
