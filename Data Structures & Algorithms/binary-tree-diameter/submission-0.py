# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_height_for_diameter(root):
            if not root:
                return 0

            l_h = max_height_for_diameter(root.left)
            r_h = max_height_for_diameter(root.right)

            self.max_diameter = max(self.max_diameter, l_h+r_h)

            return 1 + max(l_h, r_h)

        self.max_diameter = 0
        max_height_for_diameter(root)
        return self.max_diameter