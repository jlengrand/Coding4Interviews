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
    def __init__(self, value, next):
        self.value = value
        self.next = next

