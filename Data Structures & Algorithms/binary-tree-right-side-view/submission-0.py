# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            qsize = len(queue)
            for i in range(qsize):
                cur_node = queue.popleft()
                if i == qsize - 1:
                    res = cur_node.val

                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)

            result.append(res)
            
        return result