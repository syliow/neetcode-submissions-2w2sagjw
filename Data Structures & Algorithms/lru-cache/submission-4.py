class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # head (MRU) ----------- tail (LRU)
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # if key in cache
        node = self.cache.get(key)
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value

            self.remove(self.cache.get(key))
            self.insert(self.cache.get(key))
        else:
            # insert to cache
            self.cache[key] = Node(key, value)
            self.insert(self.cache.get(key))

            if len(self.cache) > self.capacity:
                # remove lru
                lru = self.tail.prev
                del self.cache[lru.key]
                self.remove(lru)

    def insert(self, node) -> None:
        # insert at head (mru), old mru become lru
        oldMru = self.head.next
        # existing node
        self.head.next = node
        oldMru.prev = node
        # new node
        node.next = oldMru
        node.prev = self.head

    def remove(self, node) -> None:
        # skip over node
        node.prev.next = node.next
        node.next.prev = node.prev
