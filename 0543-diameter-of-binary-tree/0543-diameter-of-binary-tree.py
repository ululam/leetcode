# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = None
        self.d = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.path = []
        self.walk(root)

        # print (" -> ".join([str(n.val) for n in self.path]))

        return self.d

    # Returns tuple: radius of the node, path of that radius
    def walk(self, node:TreeNode) -> (int, list):
        if not node:
            return 0, []
        leftR, leftPath = self.walk(node.left) 
        rightR, rightPath = self.walk(node.right)

        if self.d < leftR + rightR:
            self.d = leftR + rightR
            self.path = leftPath + [node] + rightPath

        if leftR > rightR:
            return 1 + leftR, leftPath + [node]
        return 1 + rightR, rightPath + [node]
         