from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting, we must already have a tree/root
        # if value is less than self.value, go left
        # make a new tree/node if empty, otherwise keep going
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            # ^ if greater than or equal to, then go right, make
            # a new tree/node if empty, otherwise keep going
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # go left or right based on smaller or larger
        if target == self.value:
            return True  # if tree contains the value, this is the BASE CASE
        if target < self.value:
            if self.left is None:  # go left
                return False  # means there was nothing there to the left
            else:
                return self.left.contains(target)  # else, recurse!
        else:
            if self.right is None:  # same to the right side
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # if right exists, go right. Otherwise return self.value
        if self.right:
            return self.right.get_max()  # recursion
        else:
            return self.value  # if nothing to the right

    def for_each(self, cb):
        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach
        cb(self.value)  # recursive solution
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # ITERATIVE APPROACH:
        # use a loop and a stack that was imported
        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
