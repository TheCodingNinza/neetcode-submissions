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
    private Integer smallestNumber;
    
    public int kthSmallest(TreeNode root, int k) {
        this.smallestNumber = null;
        bfs(root, k, 0);
        return smallestNumber;
    }

    private int bfs(TreeNode currentNode, int k, int currentCount){
        
        if(currentNode == null)
            return currentCount;   
        int leftValue = bfs(currentNode.left, k, currentCount);
        if(leftValue + 1 == k){
            this.smallestNumber = currentNode.val;
        }
            
        int rightValue = bfs(currentNode.right, k, leftValue + 1);
        return rightValue;    
    }
}
