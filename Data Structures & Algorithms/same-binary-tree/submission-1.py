# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        navigationPathP = [];
        navigationPathP.append("root");
        navigationPathQ = [];
        navigationPathQ.append("root");
        self.navigate(p, navigationPathP);
        self.navigate(q, navigationPathQ);
        return navigationPathP == navigationPathQ;

    def navigate(self, node: Optional[TreeNode], navigationPath: list[str]) -> None:
        if(node is None):
            return;
        navigationPath.append(node.val)
        navigationPath.append("left")
        self.navigate(node.left, navigationPath)
        navigationPath.append("right")
        self.navigate(node.right, navigationPath)       