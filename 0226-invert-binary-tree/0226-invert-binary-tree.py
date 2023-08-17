# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # return self.invertTreeRecursively(root)
        return self.invertTreeIteratively(root)
        
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
        # We create a list (or a queue) of elements
        # First, we add root there
        # We run a cycle and take a first element of a queue
        # We swap it's children
        # If left child is not null, we add it to the queue
        # Same for the right
        if not root:
            return root
        from collections import deque
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root

