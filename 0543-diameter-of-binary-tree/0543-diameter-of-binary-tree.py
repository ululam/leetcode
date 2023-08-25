# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        return self.dRec(root)[0]

    def dRec(self, root):
        if not root:
            return 0,0

        dLeft, rLeft = self.dRec(root.left)
        dRight, rRight = self.dRec(root.right)
        maxD = max(dLeft, dRight)
        maxD = max(rLeft + rRight, maxD)

        return maxD, max(rLeft, rRight) + 1

    
    def dIter(self, root):
        pass

        # we need to iterate over the tree, either recursively or iteratively
        # for each node, we need to calculate its D = Rl + Rr and R = max(Rl, Rr)
        # we store Dmax in var
        #
