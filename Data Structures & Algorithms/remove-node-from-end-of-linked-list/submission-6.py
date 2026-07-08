# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # do we need dummy? yes bcs we might remove head
        # pattern: slow fast pointer, slow can stop in front of the node need remove
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        while n > 0:
            n -= 1
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # now slow is one node in front of node we want to remove
        slow.next = slow.next.next
        return dummy.next
