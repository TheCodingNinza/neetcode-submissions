# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, -101)
        return self.ans

    def traverse(self, node: Optional[TreeNode], maxVal: int):
        if not node:
            return

        if maxVal <= node.val:
            self.ans += 1
            maxVal = node.val    

        self.traverse(node.left, maxVal)
        self.traverse(node.right, maxVal)

             
        