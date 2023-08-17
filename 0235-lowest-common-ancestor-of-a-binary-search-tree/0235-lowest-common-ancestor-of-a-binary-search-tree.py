# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestorIter(root, p, q)

    def lowestCommonAncestorRec(self, root, p, q):
        # Traverse the tree
        # If current node << p,q => treverse node.left
        # If current node >> p,q => treverse node.right
        # Otherwise, return node
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root

    def lowestCommonAncestorIter(self, root, p, q):
        node = root

        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node
