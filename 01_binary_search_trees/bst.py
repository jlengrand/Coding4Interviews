"""
Binary Search Tree Implementation
@jlengrand
2013/07
"""

class BinarySearchTree():
    """
    Defines a complete binary search Tree.
    A binary search tree has a root node.
    We also add a size to the search tree, that corresponds to the number of
    nodes it has.
    """
    def __init__(self):
        self.size = 0
        self.root_node = None

class BinarySearchNode():
    """
    Defines any node of the Binary Search Tree.
    A node has at most 2 children, and it has a value.
    It also must have a parent
    """
    def __init__(self, value, parent):
        self.parent_node = parent
        self.node_value = value

        self.left_child = None
        self.right_child = None
