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
    private boolean isSubRoot = false;  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {

        StringBuilder navigationPathRoot = new StringBuilder();
        StringBuilder navigationPathSubRoot = new StringBuilder();
        navigate(subRoot, navigationPathSubRoot);
        navigateStartingFromCurrentNode(root, navigationPathSubRoot, subRoot);
        return isSubRoot;
    }

    private void navigate(TreeNode node, StringBuilder sb){
        sb.append(node.val);
        if(node.left != null){
            sb.append("left");
            navigate(node.left, sb);
        }
        if(node.right != null){
            sb.append("right");
            navigate(node.right, sb); 
        }   
    }

    private void navigateStartingFromCurrentNode(TreeNode currentNode, StringBuilder sb, TreeNode subTree){
        if(currentNode == null)
            return;

        StringBuilder sbNew = new StringBuilder();
        navigate(currentNode, sbNew);
        if(sbNew.toString().equals(sb.toString())){
            this.isSubRoot = true;
            return;
        }
        navigateStartingFromCurrentNode(currentNode.left, sb, subTree);
        navigateStartingFromCurrentNode(currentNode.right, sb, subTree);

    }
}
