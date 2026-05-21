# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reorder the nodes = swap
        # First -> Last -> Second -> Second Last ...
        #split, reverse 2nd half and merge both list
        #no need dummy bcs head is always the same

        #1. split
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is one node in front of second
        second = slow.next
        slow.next = prev = None

        #2. reverse
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #3. merge
        #reset pointers
        second = prev
        first = head

        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            #first -> second -> tmp1
            first.next = second
            second.next = tmp1
            #move both pointer forward
            first = tmp1
            second = tmp2
        
