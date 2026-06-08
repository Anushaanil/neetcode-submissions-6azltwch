# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []

        def serialize_helper(root):
            if root is None:
                self.result.append("N")
                return None
            
            self.result.append(f"{root.val}")

            serialize_helper(root.left)
            serialize_helper(root.right)

        serialize_helper(root)

        return ','.join(self.result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = 0

        def serialize_helper(data):
            
            if data[self.idx] == "N":
                self.idx +=1
                return None
            
            root = TreeNode(data[self.idx])

            self.idx +=1

            root.left = serialize_helper(data)
            root.right = serialize_helper(data)

            return root

        data = data.split(',')
        return serialize_helper(data)