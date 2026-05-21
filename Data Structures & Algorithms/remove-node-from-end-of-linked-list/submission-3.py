# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return head
        # remove node = skip node
        # need dummy? Yes bcs we might remove the head
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while n > 0:
            # move fast forward first to create a gap
            fast = fast.next
            n -= 1
        # not fast and fast.next bcs we only move once
        while fast:
            slow = slow.next
            fast = fast.next
        # now slow is one node infront of the node we want to skip
        slow.next = slow.next.next
        return dummy.next
