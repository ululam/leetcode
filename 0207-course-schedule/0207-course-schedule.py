from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        nbors = [[] for _ in range(numCourses)]

        for pr in prerequisites:
            indegree[pr[0]] += 1
            nbors[pr[1]].append(pr[0])

        queue = deque()
        for i, ind in enumerate(indegree):
            if ind == 0:
                queue.append(i)
        
        coursesVisited = 0
        while queue:
            i = queue.popleft()
            coursesVisited += 1
            for nb in nbors[i]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    queue.append(nb)

        return coursesVisited == numCourses

