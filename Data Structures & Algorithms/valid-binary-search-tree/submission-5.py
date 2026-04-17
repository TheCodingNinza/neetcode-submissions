# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.traverse(root)
        return self.ans

    def traverse(self, node: TreeNode) -> Tuple[int,int]:
        # if not self.ans:
        #     return -5555

        print(f"node: {node.val}")

        left = None
        right = None

        if node.left:
            left = self.traverse(node.left)

        if node.right:
            right = self.traverse(node.right)

        if left != None and right != None:
            if node.val <= left[1] or node.val >= right[0]:
                self.ans = False
            valMin = min (left[0], right[0], node.val)    
            valMax= max (left[1], right[1], node.val)    
            print(f"val: {valMin, valMin}")    
            return (valMin, valMax)    

        elif left == None and right != None:
            if node.val >= right[0]:
                self.ans = False
            valMin = min (right[0], node.val)    
            valMax= max (right[1], node.val)    
            print(f"val: {valMin, valMin}")    
            return (valMin, valMax)   

        elif left != None and right == None:
            if node.val <= left[1]:
                self.ans = False
            valMin = min (left[0], node.val)    
            valMax= max (left[1], node.val)    
            print(f"val: {valMin, valMin}")    
            return (valMin, valMax)

        else:
            valMin = node.val    
            valMax = node.val    
            print(f"val: {valMin, valMin}")    
            return (valMin, valMax)              


        