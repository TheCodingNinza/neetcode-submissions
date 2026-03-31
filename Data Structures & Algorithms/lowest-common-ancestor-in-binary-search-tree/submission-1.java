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
    TreeNode ancestor = null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        bfs(root, p, q);
        
        return this.ancestor;

    }

    private TreeNode bfs(TreeNode parent, TreeNode p, TreeNode q){
        
        if(parent == null)
            return null;
        
        
        TreeNode leftChild = bfs(parent.left, p, q );
        TreeNode rightChild = bfs(parent.right, p , q);
        
        if(leftChild != null && rightChild != null){
            this.ancestor = parent;
            return null;
        }else if(leftChild != null && rightChild == null){
            if(parent.val == p.val || parent.val == q.val){
                this.ancestor = parent;
                return null;
            }else{
                return leftChild;
            }
        }else if(leftChild == null && rightChild != null){
            if(parent.val == p.val || parent.val == q.val){
                this.ancestor = parent;
                return null;
            }else{
                return rightChild;
            }
        }else{
            if(parent.val == p.val || parent.val == q.val){
                return parent;
            }else{
                return null;
            }
        }
    }
}
