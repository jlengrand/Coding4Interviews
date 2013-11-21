"""
HashMap Table Implementation

Collisions are not handled in this version.

@jlengrand
2013/11
"""

import abc

class HashMapItem():
	"""
	The type of Object that is ingested by HashMap
	It can be as simple as a String, but must have a get_value() method.
	The get_value method will be used to calculate the hash key
	"""
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod	
	def get_value(self):
		return NotImplementedError("Method has to be implemented by sub classes")

class HashMap():
	def __init__(self, hash_size=513):
		self._hash_size = hash_size
		self._size = 0
		self.hmap = [None] * self._hash_size
		
	def add(self, value):
		"""
		Adds the provided value to the hashmap.
		Raises an Exception if a collision is detected
		"""
		key = self._hash(value)
		if self.hmap[key] == None:
			self.hmap[key] = value
			self._size += 1
		else: 
			raise Exception("Collision detected at index %d", key)
	
		# TODO: Keep implementing
	
	def get(self, value):
		"""
		Finds the element in the hash table that may contain the id for 
		the string we are looking for
		"""
		key = self._hash(value)
		return self.hmap[key]		
	
	def size(self):
		return self._size
	
	def _hash(self, value):
		"""
		Generates a hash for the given value.
		The input is expected to be a String, with only ASCII characters.
		
		# hash function taken from HT3.
		# We shift and add : << 4 is a *16
		"""
		if len(value) < 1:
			raise Exception("Size of value must be greater than one")
		
		h = 0
		for letter in value:
			h = (h << 4) + ord(letter)
			
		return h % self._hash_size

	
