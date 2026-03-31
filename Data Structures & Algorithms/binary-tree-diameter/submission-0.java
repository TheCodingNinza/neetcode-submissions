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
    private int maxDiameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        findDepth(root);
        return this.maxDiameter;
    }
    
    private int findDepth(TreeNode node){
        if(node == null)
            return 0;
        int leftDepth  = findDepth(node.left);
        int rightDepth = findDepth(node.right);
        this.maxDiameter = Math.max(leftDepth + rightDepth, maxDiameter);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
