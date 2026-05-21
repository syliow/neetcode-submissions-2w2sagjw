# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #dunnid dummy
        slow = head
        fast = head

        #we use fast and fast.next when fast moves twice
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #if cycle, eventually they will meet
            if slow == fast:
                return True #cycle
        return False
