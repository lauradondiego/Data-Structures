from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
# it makes sense to use a queue for our cache

    def __init__(self, limit=10):
        self.limit = limit  # this keeps track of max # of nodes
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            # ^ if the key exists in our storage dictionary
            node = self.storage[key]
            # ^ then retrieve the node associated with that key
            self.dll.move_to_front(node)
            # ^ move it to the head, since its the most recently used
            return node.value[1]
            # ^ return the value associated with that node
        else:
            return None
            # ^ if it cant find it, it does not exist

    # operation that fetches a value given a key.
    # When a key-value pair is fetched from the cache,
    # we'll go through the same priority-increase dance
    # that also happens when a new pair is added to the cache.

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):  # adds key,value pairs to the cache
        if key in self.storage:  # if they key exists already
            node = self.storage[key]  # retrieve node associated w that key
            node.value = (key, value)
            self.dll.move_to_front(node)
            # ^ move to the front since its the most recently used
            return
        if self.size == self.limit:  # if cache is full at limit 10
            # if key is not in cache and the cache is full,
            del self.storage[self.dll.tail.value[0]]
            # ^ then need to delete the oldest in cache to make room for the new one being added
            self.dll.remove_from_head()  # also delete from dll
            # delete the key for the last (tail) value in the dictionary
            self.size -= 1  # reduce length by 1
            self.dll.add_to_head((key, value))
            # ^ now add new value to the head of the dll
            self.storage[key] = self.dll.head
            # ^ aso add the key to the storage dictionary
            self.size += 1  # increase the length counter

    ## NOTES ##
    # LRU cache (Least Recently Used) cache is an in-memory storage structure
    # that adheres to the Least Recently Used caching strategy.
    # (Discards the least recently used items first.)
    # a data structure that keeps track of the order in which elements
    # (which take the form of key-value pairs) it holds are added and updated.
    # has a max number of entries it can hold. Once the cache is holding the
    # max number of entries, if a new entry is inserted, another pre-existing
    # entry needs to be evicted from the cache. Bc the cache is using a
    # least-recently used strategy, the oldest entry
    # (the one that was added/updated the longest time ago) is removed to make
    # space for the new entry.

    # there is no explicit remove method
