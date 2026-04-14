# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append((0, root))
        ans = []
        previousLevel = 0
        arr = []
        while que:
            (level, node) = que.popleft()
            if level != previousLevel:
                ans.append(arr)
                arr = []
            arr.append(node.val)
            if node.left:
                que.append((level + 1, node.left))
            if node.right:
                que.append((level + 1, node.right))    
            previousLevel = level

        if arr:
            ans.append(arr)        

        return ans