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
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
            StringBuilder navigationPathP = new StringBuilder("root");
            navigate(p, navigationPathP);
            StringBuilder navigationPathQ = new StringBuilder("root");
            navigate(q, navigationPathQ);
            return navigationPathP.toString().equals(navigationPathQ.toString()); 
    }

    private void navigate(TreeNode node, StringBuilder navigationPath){
        
        if(node == null){
            return;
        }
        navigationPath.append(node.val);
        navigationPath.append("left");
        navigate(node.left, navigationPath);
        navigationPath.append("right");
        navigate(node.right, navigationPath);
    }
}
