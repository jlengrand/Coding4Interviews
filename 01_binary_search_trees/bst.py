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
        """
        Adds the input value in the right position of the binary search Tree
        The rule is, left children of a node have a value < than the value
        of the node.
        Right children of a node conversely have a value >= of the value of
        the node.
        """
        if self.size == 0:
            self.root_node = BinarySearchNode(value, None)  # root node has no parent

        else:
            node = self.root_node
            is_left = None
            while(node is not None):
                ptr_node = node  # keep parent in memory
                if node.value > value:  # we go to the left child
                    node = node.left_child
                    is_left = True
                else:  # we move to the right child. This means = case too
                    node = node.right_child
                    is_left = False

            # we reached a leaf
            node = BinarySearchNode(value, ptr_node)
            if is_left:
                ptr_node.left_child = node
            else:
                ptr_node.right_child = node

        self.size += 1

    def max(self):
        """
        Returns the highest node value of the tree.
        Otherwise, returns None
        """
        if self.size == 0:
            return None
        else:  # we have nodes in the tree
            node = self.root_node
            while(node.has_right_child()):
                node = node.right_child

            # we have the leaf
            return node.value

    def min(self):
        """
        Returns the lowest node value of the tree.
        Otherwise returns None
        """
        if self.size == 0:
            return None
        else:  # we have nodes in the tree
            node = self.root_node
            while(node.has_left_child()):
                node = node.left_child

            # we have the leaf
            return node.value

    def __str__(self):
        """
        Prints a nice version of the binary search node
        """
        max_iter = 1000000000  # max number of nodes
        ite = 0
        ret = ""
        node = self.root_node

        top = False  # dictates when to climb one level
        while(ite < max_iter):
            while (node.has_left_child()):
                node = node.left_child
                top = True
            ret += str(node.value) + " "
            if top:  # we need to climb one level
                node = node.parent
                top = False
                ret += str(node.value) + " "
            if (not node.has_right_child()):
                return ret.strip()  # removes superflous spaces
            else:
                node = node.right_child
            ite += 1
        return None  # problem

    @staticmethod
    def is_search_tree(a_tree_root):
        """
        Returns true of the input binary tree is a valid search binary tree.
        """
        #If I don't follow the rule, no need to check further
        if not BinarySearchTree.is_search_node(a_tree_root):
            return False
        else:
            left = BinarySearchTree.is_search_tree(a_tree_root.left_child) if a_tree_root.has_left_child() else True
            right = BinarySearchTree.is_search_tree(a_tree_root.right_child) if a_tree_root.has_right_child() else True

            return left and right
            #return (BinarySearchTree.is_search_tree(a_tree_root.left_child) and BinarySearchTree.is_search_tree(a_tree_root.right_child))

    @staticmethod
    def is_search_node(a_tree_node):
        #edge case is True
        if a_tree_node is None:
            return True

        left = (not a_tree_node.has_left_child()) or (a_tree_node.has_left_child() and a_tree_node.left_child.value <= a_tree_node.value )
        right = (not a_tree_node.has_right_child()) or (a_tree_node.has_right_child() and a_tree_node.right_child.value > a_tree_node.value )

        return (left and right)


class BinarySearchIterator():
    """
    Transforms a binary search tree into an iterator.
    Will returns the values of the tree in ascending order.
    """

    def __init__(self, tree):
        self.tree = tree
        self.node = tree.root_node
        self.max_ite = 1000000000  # max number of nodes
        self.ite = 0
        self.pos = "left"

    def __iter__(self):
        return self

    def go_left(self):
        while(self.node.has_left_child()):
            self.node = self.node.left_child

        ret_val = self.node.value

        self.pos = "top"  # next state is top

        return ret_val

    def go_top(self):
        self.node = self.node.parent
        ret_val = self.node.value

        self.pos = "right"

        return ret_val

    def go_right(self):
        if (not self.node.has_right_child()):
            raise StopIteration  # end condition. We reached the end of tree
        else:
            self.node = self.node.right_child
            if self.node.has_left_child():
                self.pos = "left"
            else:
                self.pos = "right"

        ret_val = self.node.value
        return ret_val  # we dont change node here

    def next(self):
        if self.ite > self.max_ite:
            print "max limit reached!"
            raise StopIteration  # max number of elements

        print self.pos
        if self.pos == "left":
            return self.go_left()
        elif self.pos == "top":
            return self.go_top()
        elif self.pos == "right":
            try:
                return self.go_right()
            except StopIteration:
                raise StopIteration
        else:
            print "problem!"
            raise StopIteration  # problem somewhere

        self.ite += 1

        # max_iter = 1000000000  # max number of nodes
        # ite = 0
        # ret = ""
        # node = self.root_node

        # top = False  # dictates when to climb one level
        # while(ite < max_iter):
        #     while (node.has_left_child()):
        #         node = node.left_child
        #         top = True
        #     ret += str(node.value) + " "
        #     if top:  # we need to climb one level
        #         node = node.parent
        #         top = False
        #         ret += str(node.value) + " "
        #     if (not node.has_right_child()):
        #         return ret.strip()  # removes superflous spaces
        #     else:
        #         node = node.right_child
        #     ite += 1
        # return None  # problem



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
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def __str__(self):
        """
        prints a single tree node.
        """
        ret = ""
        if self.has_left_child():
            ret += str(self.left_child.value) + " "

        ret += str(self.value)

        if self.has_right_child():
            ret += " " + str(self.right_child.value)

        return ret
