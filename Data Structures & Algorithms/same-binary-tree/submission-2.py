# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_sign = {}
        q_sign = {}
        
        self.solve(p, p_sign, 0)
        self.solve(q, q_sign, 0)

        return p_sign == q_sign

    def solve(self, node: Optional[TreeNode], sign: Dict[int, int], index: int) -> None:
        if not node:
            return

        sign[index] = node.val

        self.solve(node.left, sign, (2 * index) + 1)
        self.solve(node.right, sign, (2 * index) + 2)

        