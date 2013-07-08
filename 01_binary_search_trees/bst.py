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

    def add(self, value):
        if self.size == 0:
            self.root_node = BinarySearchNode(value, None) # root node has no parent

        else:
            node = self.root_node
            is_left = None
            while(node != None):
                ptr_node = node # keep parent in memory
                if node.value > value:  # we go to the left child
                    node = node.left_child
                    is_left = True
                else: # we move to the right child
                    node = node.right_child
                    is_left = False

            # we achieved a leaf
            node = BinarySearchNode(value, ptr_node)
            if is_left:
                ptr_node.left_child = node
            else:
                ptr_node.right_child = node

        self.size += 1

class BinarySearchNode():
    """
    Defines any node of the Binary Search Tree.
    A node has at most 2 children, and it has a value.
    It also must have a parent
    """
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value

        self.left_child = None
        self.right_child = None

    def has_left_child(self):
        return not(self.left_child is None)

    def has_right_child(self):
        return self.right_child is not None

