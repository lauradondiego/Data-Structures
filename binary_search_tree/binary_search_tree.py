from dll_stack import Stack
from dll_queue import Queue

# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value  # the value at the current node
        self.left = None  # reference to this node's left child
        self.right = None  # reference to this node's right child

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
        if not self:
            return None  # check if tree is empty
        # if right exists, go right. Otherwise return self.value
        if not self.right:
            return self.value  # if nothing to the right
        return self.right.get_max()  # recursion

    def for_each(self, cb):
        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach

        ### RECURSIVE APPROACH COMMENTED OUT BELOW ###
        # cb(self.value)  # recursive solution
        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)

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
        if self.value:  # if it exists
            if self.left:
                # ^ first recur on the left child
                self.left.in_order_print(self.left)
            print(self.value)
            # ^ then print the data of the node
            if self.right:
                # ^ now check the right side if it exists
                self.right.in_order_print(self.right)
            print(self.value)  # print the right side

    # ^if there is a left node, then pass that into the function to print it.
    # ^You can’t just assume there is a self.left
    # ^it will keep looking for a left child until it finally
    # ^can’t find one and then it will start printing them.
    # ^Then it will call the right side

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):  # use a queue (FIFO)
        queue = Queue()
        # ^ this keeps the nodes we need to print
        queue.enqueue(node)
        # ^ this puts the current node in the queue by callling enqueue
        while queue.len() > 0:
            # ^ as long as the queue is not empty
            current = queue.dequeue()
            print(current.value)  # print it
            if current.left:
                # ^ now look to see if that node has a left child
                queue.enqueue(current.left)
                # ^ if so, add that node to the queue
            if current.right:
                # ^ if it has a right child, add that one as well
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):  # use a stack add and remove from head
        stack = Stack()  # set up an empty stack
        stack.push(node)  # push a node onto the stack
        while stack.len() > 0:  # as long as there are nodes in the stack
            current = stack.pop()  # pop off from the top of the stack
            print(current.value)
            if current.left:  # check if the node has a left child
                # if so, push that child onto the stack
                stack.push(current.left)
            if current.right:  # now check if that node has a right child
                stack.push(current.right)  # if so, push that onto the stack

        # STRETCH Goals -------------------------
        # Note: Research may be required

        # Print In-order recursive DFT

    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
