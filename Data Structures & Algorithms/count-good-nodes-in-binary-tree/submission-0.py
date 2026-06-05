# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def compute_max_good_nodes_count(root, max_so_far):
            if not root:
                return 0

            count = 0
            
            if root.val >= max_so_far:
                count+=1
            
            new_max = max(max_so_far, root.val)

            l_count = compute_max_good_nodes_count(root.left, new_max)
            r_count = compute_max_good_nodes_count(root.right, new_max)

            return count + l_count + r_count

        return compute_max_good_nodes_count(root, root.val)