# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            current_level_nodes = []

            for _ in range(len(queue)):
                cur_node = queue.popleft()
                current_level_nodes.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                    
                if cur_node.right:
                    queue.append(cur_node.right)
                    
            if current_level_nodes: result.append(current_level_nodes)

        return result