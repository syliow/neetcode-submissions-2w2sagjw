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
        # hashmap: [og_node: clone_node]
        refMap = {}
        # two pass: clone val first, then random and next later
        # create a new node with old node as ref that only has val
        cur = head
        while cur:
            copy = Node(cur.val)
            refMap[cur] = copy
            cur = cur.next

        # 2nd pass: map next and random to copy list
        # reset pointer
        cur = head
        while cur:
            # how do we get ref from og
            copy = refMap.get(cur)  # we passed in whole node -> refMap[cur] = copy
            copy.next = refMap.get(cur.next)
            copy.random = refMap.get(cur.random)
            cur = cur.next
        # return head of copied list
        return refMap.get(head)
