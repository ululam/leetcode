# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidRec(root, -math.inf, math.inf)
        # return self.isValidIter(root)

    # [1,2,3,4,5] 
    def isValidRec(self, node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        
        return self.isValidRec(node.left, low, node.val) and self.isValidRec(node.right, node.val, high)

    def isValidIter(self, root):
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if node.val <= low or node.val >= high:
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        return True