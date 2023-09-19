from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjacents = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adjacents[pre[1]].append(pre[0])
            indegree[pre[0]] += 1 
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for nbor in adjacents[node]:
                indegree[nbor] -= 1
                if indegree[nbor] == 0:
                    queue.append(nbor)
        
        return nodesVisited == numCourses