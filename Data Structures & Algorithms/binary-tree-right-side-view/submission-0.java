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
    public List<Integer> rightSideView(TreeNode root) {
        List<List<Integer>> levelWiseNodeList = new ArrayList<>();
        bfs(root, 0, levelWiseNodeList);
        List<Integer> ans = new ArrayList<>();
        for(List<Integer> nodes: levelWiseNodeList){
            ans.add(nodes.get(nodes.size() - 1));
        }
        return ans;
    }

    private void bfs(TreeNode currentNode, int currentLevel, List<List<Integer>> levelWiseNodeList){
        if(currentNode == null)
            return;
        for(int i = levelWiseNodeList.size(); i < currentLevel + 1; i++){
            levelWiseNodeList.add(new ArrayList<>());
        }
        levelWiseNodeList.get(currentLevel).add(currentNode.val);
        bfs(currentNode.left, currentLevel + 1, levelWiseNodeList);
        bfs(currentNode.right, currentLevel + 1, levelWiseNodeList);
    }
}
