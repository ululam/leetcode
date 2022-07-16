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
    public int diameterOfBinaryTree(TreeNode root) {
        RD rd = new RD();
        radius(root, rd);
        return rd.diameter;
    }
    
    private int radius(TreeNode node, RD maxRD) {
        int rightR = node.right != null ? radius(node.right, maxRD) : 0;
        int leftR = node.left != null ? radius(node.left, maxRD) : 0;
        int curRadius = Math.max(rightR, leftR) + 1;
        int currentDiameter = rightR + leftR;
        maxRD.diameter = Math.max(currentDiameter, maxRD.diameter);
        return curRadius;
    }
}

class RD {
    int diameter;
}