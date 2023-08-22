class Solution(object):
    # 3 => 1,1,1 & 1,2 & 2,1 = 3
    # 4 => 1,1,1,1 & 1,2,1 etc...
    #
    # N: (N-1)+1 or (N-2)+2 
    def __init__(self):
        self.staircase = {}

    def climbStairsMemo(self, n):
        if n < 3:
            return n
        steps = self.staircase.get(n)
        if not steps:
            steps = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.staircase[n] = steps
        
        return steps

    def climbStairs(self, n):
        if n < 3:
            return n
        steps = [0] * (n+1)
        steps[1] = 1
        steps[2] = 2
        for i in range (3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]