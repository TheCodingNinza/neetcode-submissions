# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      self.traverse(root)
      return self.ans

    def traverse(self, node: Optional[TreeNode]) -> Tuple[int]:
        
        if not node:
            return ()
        
        leftVal = self.traverse(node.left)
        rightVal = self.traverse(node.right)
        finalVal = tuple(map(lambda x: x + node.val, leftVal)) + tuple(map(lambda x: x + node.val, rightVal)) + (node.val,)
        print(f"node: {node.val}") 
        print(f"finalVal: {finalVal}")

    
            
        
        if self.ans != None:
            print(f"before ans: {self.ans}")
            print("in self.ans 1")
            self.ans = max(max(leftVal, default=0) + max(rightVal, default=0) + node.val, self.ans, node.val, node.val + max(rightVal, default=0), node.val + max(leftVal, default=0))
            print(f"after ans: {self.ans}")
        else:
            print(f"before ans: {self.ans}")
            print("in self.ans 2")
            self.ans =  max(max(leftVal, default=0) + max(rightVal, default=0) + node.val, node.val, node.val + max(rightVal, default=0), node.val + max(leftVal, default=0)) 
            print(f"after ans: {self.ans}") 
           
        # print(f"ans: {self.ans}")
        return finalVal        