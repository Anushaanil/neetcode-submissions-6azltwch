# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildHelper(left_boundary, right_boundary):
            if left_boundary > right_boundary:
                return None

            root_val = preorder[self.pre_order_index]
            root = TreeNode(root_val)
            self.pre_order_index+=1
            
            inorder_idx = self.index_map[root_val]
            root.left = buildHelper(left_boundary, inorder_idx-1)
            root.right = buildHelper(inorder_idx+1, right_boundary)

            return root
        
        self.index_map = {val:i for i, val in enumerate(inorder)}
        self.pre_order_index = 0
        return buildHelper(0, len(preorder)-1)