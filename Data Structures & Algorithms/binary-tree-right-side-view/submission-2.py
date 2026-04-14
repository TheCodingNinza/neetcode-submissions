# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque()
        ans = []
        que.append((0, root))
        previousLevel = 0
        ans.append(root.val)
        while que:
            (level, node) = que.popleft()
            if previousLevel != level:
                ans.append(node.val)
            if node.right:    
                que.append((level + 1, node.right))
            if node.left:    
                que.append((level + 1, node.left))
            previousLevel = level
        return ans    

        