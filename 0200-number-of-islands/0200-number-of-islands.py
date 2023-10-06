class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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