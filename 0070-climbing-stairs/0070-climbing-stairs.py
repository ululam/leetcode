class Solution(object):
    # 3 => 1,1,1 & 1,2 & 2,1 = 3
    # 4 => 1,1,1,1 & 1,2,1 etc...
    #
    # N: (N-1)+1 or (N-2)+2 
    def __init__(self):
        self.staircase = {}

    def climbStairs(self, n):
        if n < 3:
            return n
        steps = self.staircase.get(n)
        if not steps:
            steps = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.staircase[n] = steps
        
        return steps


