# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.lca = -505

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        twoNodesSet = {p.val, q.val}
        self.solve(root, twoNodesSet)
        return self.lca

    def solve(self, node, twoNodesSet):
        if not node:
            return -505   
        a = self.solve(node.left, twoNodesSet)
        b = self.solve(node.right, twoNodesSet)
        firstSet = {a,b}
        secondSet = {a,node.val}
        thirdSet = {b,node.val}
        if firstSet == twoNodesSet or secondSet == twoNodesSet or thirdSet == twoNodesSet:
            self.lca = node
        if a in twoNodesSet:
            return a
        elif b in twoNodesSet:
            return b
        elif node.val in twoNodesSet:
            return node.val
        else:
            return -505            

            



        