# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next is None:
            return

        # 1. find the middle pointer to split
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None

        # 2. reverse the LL from middle to end, consider it a seperate list
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp

        # 3. merge both lists accordingly
        cur = head
        while prev:
            temp1 = cur.next
            temp2 = prev.next

            cur.next = prev
            prev.next = temp1

            cur = temp1
            prev = temp2