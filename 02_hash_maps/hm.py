"""
HashMap Table Implementation

Collisions are not handled in this version.

@jlengrand
2013/11
"""

class HashMap():
	def __init__(self, hash_size=513):
		self._hash_size = hash_size
		self._size = 0
		self.hmap = [None] * self._hash_size
		
	def add(self, key, value):
		"""
		Adds the provided value to the hashmap.
		Raises an Exception if a collision is detected
		"""
		my_key = self._hash(key)
		if self.hmap[my_key] == None:
			self.hmap[my_key] = value
			self._size += 1
		else: 
			raise Exception("Collision detected at index %d", key)
	
		# TODO: Keep implementing
	
	def get(self, key):
		"""
		Finds the element in the hash table that may contain the id for 
		the string we are looking for
		"""
		my_key = self._hash(key)
		return self.hmap[my_key]		
	
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

class HMTableCollision(HashMap):
	"""
	Extension of the previous HashMap implementation that takes care of
	collisions.
	Instead of having only one slot available per index in the table, 
	each index will contain a list. This means several elements can be 
	stored with the same index.
	"""
	def add(self, key, value):
			"""
			Adds the provided value to the hashmap.
			Raises an Exception if a collision is detected
			"""
			my_key = self._hash(key)
			
			
			if self.hmap[my_key] == None:
				self.hmap[my_key] = value
				self._size += 1
			else: 
				raise Exception("Collision detected at index %d", key)
