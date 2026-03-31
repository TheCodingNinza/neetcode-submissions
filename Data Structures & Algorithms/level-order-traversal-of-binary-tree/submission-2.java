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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        bfs(root, ans, 0);
        return ans;
    }

    private void bfs(TreeNode currentNode, List<List<Integer>> ans, int currentLevel){
        if(currentNode == null)
            return;
        if(ans.size() < currentLevel + 1){
            for(int i=ans.size(); i < currentLevel + 1; i++){
                ans.add(new ArrayList<>());
            }
        }
        System.out.println("currentLevel: "+currentLevel);
        System.out.println("ansSize: "+ans.size());
        ans.get(currentLevel).add(currentNode.val);
        if(currentNode.left != null)
            bfs(currentNode.left, ans, currentLevel + 1);
        if(currentNode.right != null)    
            bfs(currentNode.right, ans, currentLevel + 1);     
    }
}
