from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # The idea is to BFS: if we calculated distances from each 0 simultanuesly, 
        # we will arrive to the correct numbers (not true for DFS, obviously)

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        matrix = [[-1 if c != 0 else 0 for c in row] for row in mat]
        queue = deque()
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        while len(queue) > 0:
            row, col, distance = queue.popleft()

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and matrix[next_row][next_col] == -1:
                    matrix[next_row][next_col] = distance + 1
                    queue.append((next_row, next_col, distance + 1))

        return matrix