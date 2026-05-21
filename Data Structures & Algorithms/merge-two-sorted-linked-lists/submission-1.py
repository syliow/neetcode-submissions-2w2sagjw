# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode() #start of list
        tail = dummy

        while list1 and list2:
            # compare both value
            if list1.val < list2.val:
                tail.next = list1
                # move pointer forward
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # move node pointer forward
            tail = tail.next
        #connect the next remaining nodes to tail
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2   
        
        return dummy.next