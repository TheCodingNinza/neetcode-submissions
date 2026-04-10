# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.ans = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftLen = self.longestPathChild(root.left)
        rightLen = self.longestPathChild(root.right)
        if abs(rightLen - leftLen) >= 2:
            self.ans = False
        return self.ans    

    def longestPathChild(self, node: Optional[TreeNode]) ->int :
        if not node:
            return 0

        leftLen = self.longestPathChild(node.left)
        rightLen = self.longestPathChild(node.right)
        
        if abs(rightLen - leftLen) >= 2:
            self.ans = False

        return max(leftLen, rightLen) + 1    
        