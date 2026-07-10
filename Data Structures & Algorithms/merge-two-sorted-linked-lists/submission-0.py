# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 or list2:
            l1_val = list1.val if list1 else 1000
            l2_val = list2.val if list2 else 1000

            if l1_val < l2_val:
                l1_node = ListNode(l1_val)
                cur.next = l1_node
                cur = cur.next
                list1 = list1.next
            else:
                l2_node = ListNode(l2_val)
                cur.next = l2_node
                cur = cur.next
                list2 = list2.next
                
        return dummy.next
            
