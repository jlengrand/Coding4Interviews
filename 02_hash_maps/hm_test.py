"""
Unit tests for the Hash Map table implementation
@jlengrand
2013/11
"""

from hm import HashMap

import unittest


class test_hash_map(unittest.TestCase):

	def test_hash_size(self):
		hm = HashMap()
		self.assertEqual(hm._hash_size, 513)
		
		hm = HashMap(1025)
		self.assertEqual(hm._hash_size, 1025)
		

	def test_size(self):
		hm = HashMap()
		self.assertEqual(hm.size(), 0)

	def test__hash(self):
		hm = HashMap()
		
		value = "a"
		self.assertEqual(hm._hash(value), ord(value))
		
		value = "test"
		self.assertEqual(hm._hash(value), 208)

		value = ""
		self.assertRaises(Exception, lambda x : hm._hash(value))

	def test_add(self):
		hm = HashMap()
		
		hm.add("a")
		self.assertEqual(hm.size(), 1)

		# Tests Collision
		self.assertRaises(Exception, lambda x : hm.add(a))
		self.assertEqual(hm.size(), 1)

	def test_get(self):
		
		hm = HashMap()
		value = ""
		self.assertRaises(Exception, lambda x : hm.get(value))
		

if __name__ == "__main__":
	unittest.main()
