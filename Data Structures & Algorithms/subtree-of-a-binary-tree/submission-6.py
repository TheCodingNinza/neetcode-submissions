# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.serialize(subRoot) in self.serialize(root)

    def serialize(self, node: Optional[TreeNode]) -> str:
        if not node:
            return "#"
        return f"^{node.val},{self.serialize(node.left)},{self.serialize(node.right)}"

