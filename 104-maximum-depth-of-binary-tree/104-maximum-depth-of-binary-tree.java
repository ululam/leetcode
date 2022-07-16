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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left),  maxDepth(root.right)) + 1;
    }

    public int maxDepthIter(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Stack<TreeNode> nodes = new Stack<>();
        Stack<Integer> depths = new Stack<>();
        int currentDepth = 0, maxDepth = 0;
        TreeNode currentNode;
        nodes.push(root);
        depths.push(1);
        
        while (!nodes.isEmpty()) {
            currentNode = nodes.pop();
            currentDepth = depths.pop();
            maxDepth = maxDepth > currentDepth ? maxDepth : currentDepth;
            if (currentNode.left != null) {
                nodes.push(currentNode.left);
                depths.push(currentDepth + 1);
            }

            if (currentNode.right != null) {
                nodes.push(currentNode.right);
                depths.push(currentDepth + 1);
            }
        }
        
        return maxDepth;
    }
}