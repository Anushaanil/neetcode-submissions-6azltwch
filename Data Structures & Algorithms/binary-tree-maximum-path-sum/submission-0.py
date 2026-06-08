# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def compute_best_path(root):
            if root is None:
                return 0
            
            l_sum = max(0, compute_best_path(root.left))
            r_sum = max(0, compute_best_path(root.right))

            total_sum = root.val + l_sum + r_sum
            self.max_sum = max(self.max_sum, total_sum)
            # always return best path found so far, choose between l & r
            return root.val + max(l_sum, r_sum)

        self.max_sum = float('-inf')
        compute_best_path(root)
        return self.max_sum