# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list into half, then add to a new list
        # no need dummy, rearrange nodes only
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # start of 2nd list [4 5 6], reverse, merge
        second = slow.next
        prev = slow.next = None
        while second:  # reverse the list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge 2 list together
        first = head
        second = prev

        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            # move pointer forward
            first = tmp1
            second = tmp2
            # if got remaining nodes
            if first:
                first = tmp1
            if second:
                second = tmp2
