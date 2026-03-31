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
    private boolean ans = true;
    public boolean isBalanced(TreeNode root) {
        findDepth(root);
        return this.ans;
    }


    private int findDepth(TreeNode node){
        if(node == null)
            return 0;
        int leftDepth  = findDepth(node.left);
        int rightDepth = findDepth(node.right);
        if(Math.abs(leftDepth - rightDepth) > 1)
            this.ans = false;
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
