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
        self.nexti = nexti

    def has_next(self):
		"""
		Returns True if the item has a next value
		"""
		return not (self.nexti is None)
		
class SingleLinkedList():
	"""
	Linked list with only one link between items.
	The list can only be traversed one way"""
	
	def __init__():
		self.root= SinglelistItem(None, None) # The head

if __name__ == "__main__":
	a = 12
	t = SingleListItem(12)
	print t.has_next()
