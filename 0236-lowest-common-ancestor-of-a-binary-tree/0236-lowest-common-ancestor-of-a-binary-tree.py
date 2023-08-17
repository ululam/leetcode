# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lac = None

    def lowestCommonAncestor(self, root, p, q):
        # return self.lowestCommonAncestorRecursive(root, p, q)
        return self.lowestCommonAncestorIterative(root, p, q)
    

    def lowestCommonAncestorIterative(self, root, p, q):
        from collections import deque
        pNode, qNode = None, None
        que = deque()
        que.append(root)
        nodeMap = {}

        while pNode is None or qNode is None:
            node = que.popleft()
            if node == p:
                pNode = node
            elif node == q:
                qNode = node
            if node.left:
                nodeMap[node.left] = node
                que.append(node.left)
            if node.right:
                nodeMap[node.right] = node
                que.append(node.right)

        # print("p: " + str(pNode))
        # print("q: " + str(qNode))
        # print(nodeMap)

        pTree = set()
        while pNode:
            pTree.add(pNode)
            pNode = nodeMap.get(pNode)
        
        lac = None
        while not lac and qNode:
            if qNode in pTree:
                lac = qNode
            qNode = nodeMap.get(qNode)
        return lac

        

    def lowestCommonAncestorRecursive(self, root, p, q):
        self.recurseTree(root, p, q)
        return self.lac

    def recurseTree(self, node, p, q):
        if not node:
            return False

        left = self.recurseTree(node.left, p, q)
        right = self.recurseTree(node.right, p, q)

        mid = node == p or node == q
        if (mid and left) or (mid and right) or (left and right):
            self.lac = node

        return mid or left or right

        
