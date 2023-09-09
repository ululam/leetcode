# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # We should go down level by level
    # At each level build a list of nodes, add to the result collection
    # and recursively call the same method, passing current level colletion
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        allLevels = [[root]] + self.nextLevel([root])
        res = []
        for level in allLevels:
            res += [[n.val for n in level]]

        return res

    def nextLevel(self, nodes: List[TreeNode]):
        nextL = []
        for n in nodes:
            if n:
                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
        return [nextL] + self.nextLevel(nextL) if nextL else []
