# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftLen = self.longestPathChild(root.left)
        rightLen = self.longestPathChild(root.right)
        self.ans = max (self.ans, rightLen + leftLen)
        return self.ans

    def longestPathChild(self, node: Optional[TreeNode]) ->int :
        if not node:
            return 0

        leftLen = self.longestPathChild(node.left)
        rightLen = self.longestPathChild(node.right)
        
        self.ans = max(self.ans, rightLen + leftLen)

        return max(leftLen, rightLen) + 1


