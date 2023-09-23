# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Recursively call paths for left and right nodes
        # Append currentPrefix -> left -> [all the left paths]
        # Same for the right
        # If root != null and has no children, append root itelf
        res = []
        if root.left:
            res += [f"{root.val}->{path}" for path in self.binaryTreePaths(root.left)]
        if root.right:
            res += [f"{root.val}->{path}" for path in self.binaryTreePaths(root.right)]

        if not res:
            return [str(root.val)]

        return res
        