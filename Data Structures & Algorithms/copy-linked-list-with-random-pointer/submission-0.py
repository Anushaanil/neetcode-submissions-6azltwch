"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list = Node(0)

        dummy = new_list
        cur = head
        nodes_dict = {}

        # assign the next pointers and create new nodes first
        while cur:
            dummy.next = Node(cur.val)
            nodes_dict[cur] = dummy.next # store old and new lists in here
            cur = cur.next
            dummy = dummy.next

        # iterate over old list to form new one again
        cur = head
        new_cur = new_list.next

        while cur:
            if cur.random:
                new_cur.random = nodes_dict[cur.random]
            
            new_cur = new_cur.next
            cur = cur.next

        return new_list.next
