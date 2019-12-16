from doubly_linked_list import DoublyLinkedList
import sys
# sys.path.append('./doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # counter to keep track of the number of elements in our queue
        self.storage = DoublyLinkedList()
        # ^ we'll use our LinkedList implementation to build the queue

    def enqueue(self, value):  # adding element to a queue
        self.storage.add_to_tail(value)
        # use add_to_tail function and pass in value from line 14
        self.size += 1
        # ^ increment our size counter by 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            # ^ decrement our counter by 1
            return self.storage.remove_from_head()
            # ^ removing the head of the linked list and return it
        else:
            return None

    def len(self):  # getting the size of the queue
        return self.size
        # just simply return the size


# NOTES
# - you cannot add or remove from the middle of a queue
# - study the doubly_linked_list file for defs
# - With a queue you remove the item least recently added
# (first-in, first-out or FIFO);
