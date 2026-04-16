class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        self.head = Node(0, 0) # LRU Anchor (Cold)
        self.tail = Node(0, 0) # MRU Anchor (Hot)
        
        # Connect anchors: [Head] <-> [Tail]
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        """Standard DLL remove: stitches neighbors together."""
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def insert(self, node):
        """MRU: Always insert at the TAIL."""
        # [Prev] <-> [Node] <-> [Tail]
        prev = self.tail.prev
        nxt = self.tail
        
        # Set node's hands
        node.prev, node.next = prev, nxt
        
        # Set neighbors' hands
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            # EVICT: The oldest (LRU) is at the HEAD
            lru = self.head.next 
            self.remove(lru)
            del self.cache[lru.key]