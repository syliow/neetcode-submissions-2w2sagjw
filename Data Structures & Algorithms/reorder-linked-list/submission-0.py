# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1: find middle of list
        #2: reverse 2nd half of list
        #3: merge both list 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the 2nd half list
        #slow stops at midpoint
        second = slow.next #the node after slow is the start of 2nd list
        slow.next = None #cut the link to seperate list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge both list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 #move pointer forwar
