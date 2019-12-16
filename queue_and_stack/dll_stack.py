import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # adds the element (value) at the top of the stack
        self.storage.add_to_head(value)
        self.size += 1
        # ^ do we need to increment here?

    def pop(self):
        # deletes the top most element of the stack
        if self.size > 0:
            self.size -= 1
            # ^ decrement our counter by 1
            return self.storage.remove_from_head()
            # ^ removing the head of the linked list and return it
        else:
            return None

    def len(self):
        return self.size

# NOTES - STACKS
# - New plates are added to the top of the stack.
# And because the plates are precious and heavy,
# only the topmost plate can be moved
# (last-in, first-out).
# To reach the plates lower down in the stack
# the topmost plates must be removed one by one.

# with a stack you remove the item most recently added
# (last-in, first-out or LIFO).
