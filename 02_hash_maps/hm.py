"""
HashMap Table Implementation

Collisions are not handled in this version.

@jlengrand
2013/11
"""

class _HashMapItem():
	"""
	Hashmap items are the objects that will be contained in my Hashmaps.
	They permit to find the correct value back, even in case of collision.
	Not all of my HashMap implementations use HMItems.
	"""
	def __init__(self, key, value):
		self.k = key
		self.v = value

class HashMap():
	"""
	This implementation does NOT use _HashMapItems
	Also, this implementation will return an error in case of a collision.
	Data will not be lost, but another key will have to be used.
	"""
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
			self.hmap[my_key] = [value]
		else:
			self.hmap[my_key].append(value)
		self._size += 1

	def get(self, key):
		"""
		Finds the element in the hash table that may contain the id for
		the string we are looking for
		"""
		my_key = self._hash(key)
		vals = self.hmap[my_key]

		if vals is None:
			return vals
		elif len(vals) == 1:
			return vals[0]
		else:
			return vals # we return all the results if there are several

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

class HashMapWithItem():
	"""
	This implementation USES _HashMapItems
	Also, this implementation will return an error in case of a collision.
	Data will not be lost, but another key will have to be used.
	"""
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

class HMNeighbourCollision():
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
		idx = self._find_free_idx(my_key)

		self.hmap[idx] = value
		self._size += 1

	def _find_free_idx(self, key):
		"""
		Given an index in the current hash table, finds the nearest
		element with a free value
		"""
		idx = key
		cur_ptr = 1
		negative = True

		while(True):
			if self.hmap[idx] == None:
				return idx
			else:
				if negative:
					idx = key - cur_ptr
					negative = False
				else:
					idx = key + cur_ptr
					negative = True
					cur_ptr += 1

	def get(self, key):
		"""
		Finds the element in the hash table that may contain the id for
		the string we are looking for
		"""
		#TODO

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
