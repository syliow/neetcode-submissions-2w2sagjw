"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        #edge case
        if not head:
            return None
        copyMap = {}

        cur = head
        while cur:
            # map ori val to map first
            copy = Node(cur.val)
            copyMap[cur] = copy
            cur = cur.next
        # 2nd pass
        cur = head
        while cur:
            copy = copyMap.get(cur)
            copy.next = copyMap.get(cur.next)
            copy.random = copyMap.get(cur.random)
            cur = cur.next

        return copyMap[head]