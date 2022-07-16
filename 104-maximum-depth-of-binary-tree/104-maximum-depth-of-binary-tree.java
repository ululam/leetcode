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
    public int maxDepth2(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left),  maxDepth(root.right)) + 1;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        LinkedList<TreeNode> nodes = new LinkedList<>();
        LinkedList<Integer> depths = new LinkedList<>();
        int currentDepth = 0, maxDepth = 0;
        
        nodes.push(root);
        depths.push(1);
        
        while (!nodes.isEmpty()) {
            TreeNode node = nodes.pollLast();
            currentDepth = depths.pollLast();
            maxDepth = maxDepth > currentDepth ? maxDepth : currentDepth;
            if (node.left != null) {
                nodes.push(node.left);
                depths.push(currentDepth + 1);
            }
            if (node.right != null) {
                nodes.push(node.right);
                depths.push(currentDepth + 1);
            }
        }
        
        return maxDepth;
    }

}