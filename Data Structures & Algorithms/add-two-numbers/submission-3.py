# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we need dummy, create new list
        dummy = ListNode(0)
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            # digit = cur node val
            # carry = next col
            digit = total % 10
            carry = total // 10

            node = ListNode(digit)
            cur.next = node
            # move pointer forward
            cur = cur.next

            # why not cur.next = l1?
            # bcs we will link the remaining l1 to the list itself
            # if remaining nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
