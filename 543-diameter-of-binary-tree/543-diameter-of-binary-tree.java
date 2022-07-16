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
        return rd.path.size() - 1;
    }
    
    private List radius(TreeNode node, RD maxRD) {
        List rightR = node.right != null ? radius(node.right, maxRD) : new ArrayList();
        List leftR = node.left != null ? radius(node.left, maxRD) : new ArrayList();
        List curRadius = rightR.size() > leftR.size() ? rightR : leftR;
        curRadius.add(0, node);
        
        int currentDiameter = rightR.size() + leftR.size();
        
        if (currentDiameter > maxRD.path.size()) {
            maxRD.path = new ArrayList(rightR);
            maxRD.path.addAll(leftR);
        }
        
        return curRadius;
    }
}

class RD {
    List path = new ArrayList();
}