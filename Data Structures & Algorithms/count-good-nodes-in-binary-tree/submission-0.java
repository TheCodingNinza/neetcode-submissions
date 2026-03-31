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
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int ans  = bfs(root, pq);
        return ans;
    }

    private int bfs(TreeNode currentNode, PriorityQueue<Integer> pq){
        if(currentNode == null)
            return 0;
        int ans = 0;
        if(pq.isEmpty() || pq.peek() <= currentNode.val){
            ans++;
        }
        PriorityQueue<Integer> newPQ = new PriorityQueue<>(Collections.reverseOrder());
        newPQ.addAll(pq);
        newPQ.add(currentNode.val);
        int rightChild = bfs(currentNode.right, newPQ);
        int leftChild = bfs(currentNode.left, newPQ);
        ans = ans + rightChild + leftChild;
        return ans;
    }
}
