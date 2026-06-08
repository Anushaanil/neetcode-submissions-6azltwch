# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.kth_smallest_node = None

        def inorder_traversal(root):
            if root is None:
                return
            
            if self.kth_smallest_node is not None:
                return
            
            inorder_traversal(root.left)

            if self.kth_smallest_node is not None:
                return
            
            self.count +=1
            
            if self.count == k:
                self.kth_smallest_node = root.val
            
            inorder_traversal(root.right)
        
        inorder_traversal(root)
        return self.kth_smallest_node