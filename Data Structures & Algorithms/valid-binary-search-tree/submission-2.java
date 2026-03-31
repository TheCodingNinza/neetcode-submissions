/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    

public boolean isValidBST(TreeNode root) {
    return bfs(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
}

private boolean bfs(TreeNode currentNode, int leftBoundary, int rightBoundary) {
    if (currentNode == null)
        return true;

    if(currentNode.val < rightBoundary && currentNode.val > leftBoundary){
        boolean rightChild = bfs(currentNode.right, currentNode.val, rightBoundary);
        boolean leftChild = bfs(currentNode.left, leftBoundary, currentNode.val);
        return rightChild && leftChild;

    }else{
        return false;
    }

}
}