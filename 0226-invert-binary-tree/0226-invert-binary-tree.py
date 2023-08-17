# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        return self.invertTreeRecursively(root)
        
    # [1,2,3] => [1, 3, 2]
    # [1,2,3,4,5,6] => [1, 3, 2, 6, 5, 4]
    def invertTreeRecursively(self, root):
        # We swap left and right nodes
        # And recursively call invertTree for left and right subtrees
        # If node is null, we just return
        # That's it
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right),  self.invertTree(root.left)
        return root

    def invertTreeIteratively(self, root):
        pass
