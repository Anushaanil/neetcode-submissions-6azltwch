# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return None

        cur = head
        total_nodes = 0

        while cur:
            total_nodes+=1
            cur = cur.next

        current_count = 0
        prev = None
        cur = head

        while cur:
            current_count +=1
            target = total_nodes - current_count + 1
            if target == n:
                if not prev:
                    return head.next
                prev.next = cur.next
                break

            prev = cur
            cur = cur.next

        return head