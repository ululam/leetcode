from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # return self.updateMatrixBFS(mat)
        return self.updateMatrixDP(mat)

    def updateMatrixBFS(self, mat: List[List[int]]) -> List[List[int]]:
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
    
        while queue:
            row, col, distance = queue.popleft()

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and matrix[next_row][next_col] == -1:
                    matrix[next_row][next_col] = distance + 1
                    queue.append((next_row, next_col, distance + 1))

        return matrix

    def updateMatrixDP(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])
                        
                    dp[row][col] = min_neighbor + 1
    
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])
                        
                    dp[row][col] = min(dp[row][col], min_neighbor + 1)

        return dp        

    def updateMatrixDP2(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [row[:] for row in mat]
        m = len(mat)
        n = len(mat[0])
        maxValue = m*m + 1
        # Bottom-Right iteration
        print (">>>> Bottom Right")
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    continue
                min_neighbour = maxValue
                if row > 0:
                    min_neighbour = min(min_neighbour, matrix[row-1][col])
                if col > 0:
                    min_neighbour = min(min_neighbour, matrix[row][col-1])
                matrix[row][col] = 1 + min_neighbour
                print(f"matrix[{row}][{col}]: {matrix[row][col]}")

        print(f"{matrix}")

        # Top-Left iteration
        print (">>>> Top Left")
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if matrix[row][col] == 0:
                    continue
                min_neighbour = maxValue
                if row < m-1:
                    min_neighbour = min(min_neighbour, matrix[row+1][col])
                if col < n-1:
                    min_neighbour = min(min_neighbour, matrix[row][col+1])
                matrix[row][col] = min(matrix[row][col], 1 + min_neighbour)
                print(f"matrix[{row}][{col}]: {matrix[row][col]}")

        return matrix