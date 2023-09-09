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
        queue = deque()
        level = 0
        queue.append(root)
        currentLevelSize = len(queue)
        levels = [[]]
        while queue:
            if currentLevelSize == 0:
                currentLevelSize = len(queue)
                level += 1
                levels.append([])
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            currentLevelSize -= 1
        return levels


    # Why its BSF? Its DFS
    def levelOrderBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        levels = []
        self.traverse(root, levels, 0)
        return levels
    
    def traverse(self, node, levels, depth):
        if len(levels) == depth:
            levels += [[]]
        levels[depth] += [node.val]
        if node.left:
            self.traverse(node.left, levels, 1 + depth)
        if node.right:
            self.traverse(node.right, levels, 1 + depth)

    # My initial solution
    def levelOrderMyInitialAndItsOK(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        levels = [[root.val]]
        self.walkLevel([root], levels)
        return levels

    def walkLevel(self, nodes: List[TreeNode], levels: List[List[int]]):
        nextLNodes = []
        for n in nodes:
            if n:
                if n.left:
                    nextLNodes.append(n.left)
                if n.right:
                    nextLNodes.append(n.right)
        if nextLNodes:
            levels += [[n.val for n in nextLNodes]]
            self.walkLevel(nextLNodes, levels) 
    # return [nextL] + self.walkLevel(nextL) if nextL else []
