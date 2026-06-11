# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we need dummy node bcs we might remove head (possible)
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        #create a gap between slow and fast
        # dummy -> head -> 1 -> 2 -> 3 -> 4 
        # slow     fast
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        #now slow is 1 node in front of the node we want to remove
        slow.next = slow.next.next
        return dummy.next