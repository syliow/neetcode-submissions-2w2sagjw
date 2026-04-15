# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            #compare nodes in both list
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next #move list1 forward
            else:
                node.next = list2
                list2 = list2.next
            
            #move node forward
            node = node.next
        #take care if we have remaining nodes
        node.next = list1 or list2
        return dummy.next