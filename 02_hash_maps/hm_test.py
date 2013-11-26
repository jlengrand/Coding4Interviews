"""
Unit tests for the Hash Map table implementation
@jlengrand
2013/11
"""

from hm import HashMap
from hm import HMTableCollision
from hm import HMNeighbourCollision

import unittest

class test_hash_map_neighbour_collision(unittest.TestCase):

	def test__find_free_idx(self):
		hm = HMNeighbourCollision()

		key = "One"
		value = "Ibiza"

		my_key = hm._hash(key)
		idx = hm._find_free_idx(my_key)
		self.assertEqual(my_key, idx)

		hm.add(key, value)
		self.assertEqual(hm.size(), 1)

		# We move one up
		idx = hm._find_free_idx(my_key)
		self.assertEqual(my_key - 1, idx)

		hm.add(key, "Ibiza2")
		self.assertEqual(hm.size(), 2)

		# We move one down
		idx = hm._find_free_idx(my_key)
		self.assertEqual(my_key + 1, idx)

		hm.add(key, "Ibiza3")
		self.assertEqual(hm.size(), 3)

		# We move two up
		idx = hm._find_free_idx(my_key)
		self.assertEqual(my_key - 2, idx)

class test_hash_map_table_collision(unittest.TestCase):

	def test_add(self):
		hm = HMTableCollision()

		hm.add("a", "Ibiza")
		self.assertEqual(hm.size(), 1)

		hm.add("a", "Ibiza2")
		self.assertEqual(hm.size(), 2)

	def test_get(self):

		hm = HMTableCollision()
		value = ""
		self.assertRaises(Exception, lambda x : hm.get(value))

		key = "One"
		value = "Ibiza"
		hm.add(key, value)

		key2 = "Two"
		value2 = "NY"
		hm.add(key2, value2)
		hm.add("Three", "Berlin")
		hm.add("Four", "Chicago")

		value3 = "Ibiza2"
		hm.add(key, value3)


		self.assertEqual(hm.size(), 5)

		self.assertEqual(hm.get(key2), value2)
		self.assertEqual(hm.get("Five"), None)
		self.assertEqual(hm.get(key), [value, value3])


class test_hash_map_with_item(unittest.TestCase):

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

		hm.add("a", "Ibiza")
		self.assertEqual(hm.size(), 1)

		# Tests Collision
		self.assertRaises(Exception, lambda x : hm.add("a", "Ibiza"))
		self.assertEqual(hm.size(), 1)

	def test_get(self):

		hm = HashMap()
		value = ""
		self.assertRaises(Exception, lambda x : hm.get(value))

		key = "One"
		value = "Ibiza"
		hm.add(key, value)

		hm.add("Two", "NY")
		hm.add("Three", "Berlin")
		hm.add("Four", "Chicago")

		self.assertEqual(hm.size(), 4)

		self.assertEqual(hm.get(key), value)
		self.assertEqual(hm.get("Five"), None)

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

		hm.add("a", "Ibiza")
		self.assertEqual(hm.size(), 1)

		# Tests Collision
		self.assertRaises(Exception, lambda x : hm.add("a", "Ibiza"))
		self.assertEqual(hm.size(), 1)

	def test_get(self):

		hm = HashMap()
		value = ""
		self.assertRaises(Exception, lambda x : hm.get(value))

		key = "One"
		value = "Ibiza"
		hm.add(key, value)

		hm.add("Two", "NY")
		hm.add("Three", "Berlin")
		hm.add("Four", "Chicago")

		self.assertEqual(hm.size(), 4)

		self.assertEqual(hm.get(key), value)
		self.assertEqual(hm.get("Five"), None)

if __name__ == "__main__":
	unittest.main()
