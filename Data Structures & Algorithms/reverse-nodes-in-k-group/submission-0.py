# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Count group first
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1
        
        #reverse
        if group == k:
            cur = self.reverseKGroup(cur, k)
            while group > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                group -= 1
            #reset pointer
            head = cur
        return head