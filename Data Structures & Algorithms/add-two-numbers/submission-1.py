# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # just bring carry over to next node, if overflow, create a new node
        # need dummy? Yes - bcs we are creatiing new list
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # we might run out of nodes
            val2 = l2.val if l2 else 0
            # calculate sum
            sum = val1 + val2 + carry
            # if num > 10 (2 digits), we only get the remainder and pass caryr to next node
            carry = sum // 10  # carry: 14 //10 -> 1
            sum = sum % 10  # sum: 4
            node = ListNode(sum)  # pass on sum as new node
            # link node with cur (cur -> node)
            cur.next = node
            cur = cur.next

            # handle remaining nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
