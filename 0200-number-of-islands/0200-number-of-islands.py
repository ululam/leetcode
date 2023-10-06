class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.numIslandsBFS(grid)

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        num = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] == '1':
                    num += 1
                    queue = [(x,y)]
                    while queue:
                        pX, pY = queue.pop()
                        if pX > 0 and grid[pX-1][pY] == '1':
                            queue.append((pX-1, pY))
                        if pX < len(grid)-1 and grid[pX+1][pY] == '1':
                            queue.append((pX+1, pY))
                        if pY > 0 and grid[pX][pY-1] == '1':
                            queue.append((pX, pY-1))
                        if pY < len(grid[pX])-1 and grid[pX][pY+1] == '1':
                            queue.append((pX, pY+1))
                        grid[pX][pY] = '0'
        return num


    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        # On each "1", trigger DFS
        num = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] == '1':
                    self._traverseTree(grid, x, y)
                    num += 1
        return num
        
    def _traverseTree(self, grid: List[List[str]], x: int, y: int):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        if x > 0:
            self._traverseTree(grid, x-1, y)
        if x < len(grid)-1:
            self._traverseTree(grid, x+1, y)
        if y > 0:
            self._traverseTree(grid, x, y-1)
        if y < len(grid[x])-1:
            self._traverseTree(grid, x, y+1)            