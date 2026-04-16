class Node:
     #L ---- LRU --- MRU --- R
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        #L ---- R
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        #prev --- node --- next
        prev = node.prev
        nxt = node.next

        #prev --- next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        #L -- Old Node (Prev) -- R
        prev = self.right.prev
        nxt = self.right
        
        #L -- Old Node -- New Node (Node) -- R
        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev
        

    def get(self, key: int) -> int:
        #if not in map, return -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #remove and insert to update to MRU
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) #update map, create link
        self.insert(self.cache[key])

        #make sure its within the capacity, del if over
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
