# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.binaryTreePathsIter(root)

    def binaryTreePathsRec(self, root: Optional[TreeNode]) -> List[str]:
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
        

    def binaryTreePathsIter(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, f"{path}->{node.left.val}"))
            if node.right:
                stack.append((node.right, f"{path}->{node.right.val}"))
        
        return res
