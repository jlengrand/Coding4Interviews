"""
Implementation of Linked Lists

@jlengrand
2013/12
"""

class SingleListItem():
    """
    Item from a Single Linked List.
    Contains only a previous next element, and a value
    """
    def __init__(self, value, nexti=None):
        self.value = value
        self.nexti = nexti # pointer of the next element in the list

    def has_next(self):
		"""
		Returns True if the item has a next value
		"""
		return not (self.nexti is None)

class SingleLinkedList():
	"""
	Linked list with only one link between items.
	The list can only be traversed one way"""

	def __init__(self):
		self._size = 0
		self._root = None # reference of the head

	def add(self, value):
		"""
		Adds a new element to the end of the list
		"""
		if self._root is None:
			# empty tree
			self._root = SingleListItem(value)
		else:
			curr = self._root
			while(curr.nexti is not None):
				#gets last item
				curr = curr.nexti

			item = SingleListItem(value)
			curr.nexti = item

		self._size += 1

	def delete_item(self, node=0):
		"""
		Deletes the nth node of the list. (0 being the first element)
		If node is None, deletes the first element of the list.
		"""
		if node == 0:
			item = self._root.nexti
			self._root = item
			self._size -= 1
		elif node >= self._size:
			raise Exception("Requested value out of list bounds")
		else:
			# I want to traverse the list only once
			# Find the element before
			# Find the element after
			# Link the element after to the element before
			# Reduce the size
			item = self._root
			for i in range(node - 1):
				item = item.nexti

			item_bef = item
			item_af = item.nexti.nexti
			item_bef.nexti = item_af

			self._size -= 1

	def delete(self, value):
		"""
		Deletes the first node in the list that contains value
		"""
		ptr=0
		item = self._root
		while(item != None):
			if item.value == value:
				self.delete_item(ptr)
				return

			item = item.nexti
			ptr += 1

		print "Going there!"
		raise Exception("Value not found in the list")

	def search(self, value):
		"""
		Returns True if the value is in the List.
		"""
		item = self._root
		while(item != None):
			if item.value == value:
				return True

			item = item.nexti

		return False

	def get(self, idx):
		"""
		Returns the element of the list located at idx
		"""
		item = self._root
		if idx == 0:
			return item.value
		elif idx >= self._size:
			raise Exception("Index is greater than the size of the list!")

		for i in range(idx):
			item = item.nexti
		return item.value

	def remove_duplicates(self):
		"""
		Removes all duplicate values from the list
		"""
		# get an array of elements
		# look at items
		# if item value is in array, remove item
		# otherwise, add value to array

		values = []
		item = self._root
		ptr = 0
		while(item is not None):
			val = item.value
			if val in values:
				self.delete_item(ptr)
				ptr -= 1
			else:
				values.append(val)

			item = item.nexti
			ptr += 1

	def remove_duplicates_light(self):
		"""
		Removes all duplicate values from the list
		NOTE: This version does not store any extra data, but will take some extra
		time to complete
		"""
		pass

	def __len__(self):
		# Returns the number of elements in the list
		return self._size

	def __str__(self):
		"""
		Prints out all values in the list
		This way of doing is not exactly clever, given the fact that I put
		everything in memory before printing
		"""
		if self._root == None:
			return "Empty List"

		to_print = ""
		curr = self._root
		to_print += str(curr.value)
		while(curr.nexti is not None):
			curr = curr.nexti
			to_print += ", " + str(curr.value)

		return to_print

if __name__ == "__main__":
	ll = SingleLinkedList()
	ll.add(3)
	ll.add(4)
	ll.add(5)
	ll.add(6)
	print ll

	ll.delete(14)