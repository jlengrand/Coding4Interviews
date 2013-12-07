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
		
	def __len__(self):
		# Returns the number of elements in the list
		return self._size
			
	def __str__(self):
		"""
		Prints out all values in the list
		"""
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
