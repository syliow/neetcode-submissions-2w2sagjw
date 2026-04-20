# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #core idea: create a gap between L  and R
        #R is x node infront of L
        dummy = ListNode(0, head)
        left, right = dummy, head
        #create gap
        while n > 0:
            right = right.next
            n -= 1
        
        #move together
        while right:
            left = left.next
            right = right.next
        #skip over the node, L is infront of the node we want to del
        left.next = left.next.next
        return dummy.next