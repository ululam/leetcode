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

    def climbStairsFib(self, n):
        if n < 3:
            return n
        prev1 = 1
        prev2 = 2
        res = 0
        for i in range (3, n+1):
            res = prev1 + prev2
            prev1 = prev2
            prev2 = res
        return res

    def climbStairs(self, n):
        sqrt5 = 5 ** 0.5
        a = (1 + sqrt5)/2
        b = (1 - sqrt5)/2

        return int( (a ** (n+1) - b ** (n+1)) / sqrt5 )