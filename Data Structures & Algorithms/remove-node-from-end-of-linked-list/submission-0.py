# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #gap between 2 pointers = n
        dummy = ListNode(0, head)
        left, right = dummy, head
        #move right first to create gap
        while n > 0:
            right = right.next
            n -= 1

        #move L and R together
        while right:
            left = left.next
            right = right.next
        
        #now L is one node in front of the node we want to del
        #skip = delete
        left.next = left.next.next
        return dummy.next
