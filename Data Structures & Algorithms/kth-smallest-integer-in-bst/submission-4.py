# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k, 0)
        return self.ans

    def traverse(self, node: Optional[TreeNode], k: int, previous: int) -> int:
        if not node:
            return 0

        left = self.traverse(node.left, k, previous)
        if previous + left + 1 == k:
            self.ans = node.val

        right = self.traverse(node.right, k, previous + left + 1)

        return left + right + 1