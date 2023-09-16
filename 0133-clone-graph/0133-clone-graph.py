"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def __init__(self):
        self.seen = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.cloneGraphBreadthFS(node)

    def cloneGraphDepthFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node in self.seen:
            return self.seen[node]

        clone_node = Node(node.val, [])
        self.seen[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors];
        return clone_node

    def cloneGraphBreadthFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = deque([node])
        self.seen[node] = Node(node.val, [])

        while queue:
            current_node = queue.popleft()
            for nbor in current_node.neighbors:
                nbor_clone = self.seen.get(nbor)
                if not nbor_clone:
                    nbor_clone = Node(nbor.val, [])                    
                    self.seen[nbor] = nbor_clone
                    queue.append(nbor)
                self.seen[current_node].neighbors.append(nbor_clone)
        
        return self.seen[node]

