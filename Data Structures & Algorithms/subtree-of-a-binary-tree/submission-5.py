# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def __init__(self):
        self.ans = False
        self.subRootSign = {}
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRootSign = {}
        self.createSignature(subRoot, 0, subRootSign)
        self.subRootSign = subRootSign
        self.traverse(root, subRoot.val)
        return self.ans

    def createSignature(self, node: Optional[TreeNode], index: int, sign: Dict[int, int]) -> None:
        if not node:
            return 
        sign[index] = node.val
        self.createSignature(node.left, 2 * index + 1, sign)
        self.createSignature(node.right, 2 * index + 2, sign)

    def traverse(self, currentNode: Optional[TreeNode], subRootVal: int) -> None:
        if self.ans:
            return
        if not currentNode:
            return
        if currentNode.val == subRootVal:
            tempSign = {}
            self.createSignature(currentNode, 0, tempSign)
            if tempSign == self.subRootSign:
                self.ans = True
                return
        self.traverse(currentNode.left, subRootVal)
        self.traverse(currentNode.right, subRootVal)

