# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #core idea: create a gap between L and R first
        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        #L stops exactly one node in front of the node we want remove
        l.next = l.next.next
    
        return dummy.next