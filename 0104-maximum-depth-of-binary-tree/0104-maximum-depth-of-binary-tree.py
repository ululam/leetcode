# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthRec(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iter
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack  = list()
        stack.append((1, root))
        depth = 0
        while len(stack) > 0:
            currentDepth, node = stack.pop()
            depth = max(depth, currentDepth)
            if node.left:
                stack.append((currentDepth+1, node.left))
            if node.right:
                stack.append((currentDepth+1, node.right))                
        
        return depth