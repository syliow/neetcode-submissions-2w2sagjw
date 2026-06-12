# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #question: do we need dummy node? yes bcs we are creating a new list
        dummy = ListNode(0, 0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            sum = value1 + value2 + carry
            #result = 0 1 (carry first)
            carry = sum // 10 #caclculate carry
            sum = sum % 10 #get single digit for node

            #create a new list
            node = ListNode(sum)
            cur.next = node
            cur = cur.next #move pointer forward

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next