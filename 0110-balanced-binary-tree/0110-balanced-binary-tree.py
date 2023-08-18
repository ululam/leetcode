# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sizes = {}

    def isBalanced(self, root):
        # Tree is balanced if:
        # - abs(len(left) - len(right)) <= 1
        # - left is balanced
        # - right is balanced
        #
        # Thus, we check that recursively for each node.
        # Len of the tree is max(left len, right len) + 1
        if not root:
            return True
        if abs(self.ln(root.left) - self.ln(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def ln(self, node):
        if not node:
            return 0
        
        size = self.sizes.get(node)
        if not size:
            size = max(self.ln(node.left), self.ln(node.right)) + 1
            self.sizes[node] = size
        else:
            print("Size is found in map")

        return size;

