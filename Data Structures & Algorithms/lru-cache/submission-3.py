class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        # head (mru) ----- tail (lru)
        self.head = ListNode(0, 0)  # key, val
        self.tail = ListNode(0, 0)
        # link together
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update val and remove it from cache
            node = self.cache[key]
            node.val = value

            self.remove(node)
        else:
            # create a new node and add to map
            node = ListNode(key, value)
            self.cache[key] = node

        # Always insert the node (new or updated) at the front
        self.insert(node)

        # check capacity
        if len(self.cache) > self.capacity:
            # remove lru
            lru = self.tail.prev
            # remove from map too
            del self.cache[lru.key]
            self.remove(lru)

    def insert(self, node):
        # head (mru) ----- tail (lru)
        # always insert at mru
        # move prev mru to lru
        # 🟢 [Head] <---> [Node A] <---> [Node B] <---> [Node C] <---> [Tail] 🔴
        oldMru = self.head.next

        # new node first
        node.prev = self.head
        node.next = oldMru

        # existing nodes
        oldMru.prev = node
        self.head.next = node

    def remove(self, node):
        # skip over node
        # head ---- tail
        node.prev.next = node.next
        node.next.prev = node.prev
