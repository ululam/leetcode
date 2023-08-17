# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lac = None

    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestorRecursive(root, p, q)
    

    def lowestCommonAncestorRecursive(self, root, p, q):
        self.recurseTree(root, p, q)
        return self.lac

    def recurseTree(self, node, p, q):
        if not node:
            return False

        left = self.recurseTree(node.left, p, q)
        right = self.recurseTree(node.right, p, q)

        mid = node == p or node == q
        if (mid and left) or (mid and right) or (left and right):
            self.lac = node

        return mid or left or right

        
