class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Iterate over grid, find ALL rotten
        # Each rotten is a tree root -- we need to BFS "in parallel"
        # Queue should contain both cells and minute marker

        # How we identify that all organes become rotten?
        # Do one more final iteration
        queue = self._getAllRotten(grid)
        if not queue:
            return -1 if self._areFreshOrangesLeft(grid) else 0
        minutes = 0
        queue.append((-1, minutes+1))
        while queue:
            x, y = queue.pop(0)
            if x == -1:
                print(f"Minutes: {minutes}")
                print(f"queue: {queue}")
                if queue:
                    minutes += 1
                    queue.append((-1, minutes+1))
                continue
            # Do the interminute rottening
            if x > 0:
                self._check1RotAndAdd(grid, queue, x-1, y)
            if x < len(grid)-1:
                self._check1RotAndAdd(grid, queue, x+1, y)
            if y > 0:
                self._check1RotAndAdd(grid, queue, x, y-1)
            if y < len(grid[x])-1:
                self._check1RotAndAdd(grid, queue, x, y+1)

        if self._areFreshOrangesLeft(grid):
            return -1
        return minutes

    def _check1RotAndAdd(self, grid, queue, x, y):
        if grid[x][y] == 1:
            grid[x][y] = 2
            queue.append((x,y))


    def _getAllRotten(self, grid):
        res = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 2:
                    res.append((x,y))
        return res

    def _areFreshOrangesLeft(self, grid):
        for row in grid:
            for col in row:
                if col == 1:
                    return True
        return False