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


# TESTS
# print(Queue.enqueue(5))  # prints True
# print(Queue.enqueue(6))  # prints True
# print(Queue.enqueue(9))  # prints True
# print(Queue.enqueue(5))  # prints False
# print(Queue.enqueue(3))  # prints True
# print(Queue.len())  # prints 4
# print(Queue.dequeue())  # prints 5
# print(Queue.dequeue())  # prints 6
# print(Queue.dequeue())  # prints 9
# print(Queue.dequeue())  # prints 3
# print(Queue.len())  # prints 0
# print(Queue.dequeue())  # prints Queue Empty!

# NOTES
# - you cannot add or remove from the middle of a queue
