# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, -101)
        

    def traverse(self, node: Optional[TreeNode], maxVal: int) -> int:
        if not node:
            return 0

        count = 0
        if maxVal <= node.val:
            maxVal = node.val
            count = 1    

        leftVal = self.traverse(node.left, maxVal)
        rightVal = self.traverse(node.right, maxVal)

        return leftVal + rightVal + count

             
        