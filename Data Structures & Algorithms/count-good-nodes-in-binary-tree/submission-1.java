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
    public int goodNodes(TreeNode root) {
        int ans  = bfs(root, -101);
        return ans;
    }

    private int bfs(TreeNode currentNode, int maxValue){
        if(currentNode == null)
            return 0;
        int ans = 0;
        if(maxValue <= currentNode.val){
            maxValue = currentNode.val;
            ans++;
        }
        int rightChild = bfs(currentNode.right, maxValue);
        int leftChild = bfs(currentNode.left, maxValue);
        ans = ans + rightChild + leftChild;
        return ans;
    }
}
