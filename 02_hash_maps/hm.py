"""
HashMap Table Implementation
@jlengrand
2013/11
"""

class HashMap():
	def __init__(self):
		self._size = 0
		
	def size(self):
		return self._size
	
	def _hash(self, value):
		if len(value) < 1:
			raise Exception("Size of value must be greater than one")
		return 1

	
