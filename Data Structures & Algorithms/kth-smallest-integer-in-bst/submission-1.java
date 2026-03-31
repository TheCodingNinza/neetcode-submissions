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
        System.out.print("currentNode: "+currentNode.val);
        System.out.println(" currentCount: "+currentCount);    
        int leftValue = bfs(currentNode.left, k, currentCount);
        System.out.println("leftValue: "+leftValue);
        if(leftValue + 1 == k){
            System.out.println("Am I getting executed twice");
            this.smallestNumber = currentNode.val;
        }
            
        int rightValue = bfs(currentNode.right, k, leftValue + 1);
        return rightValue;    
    }
}
