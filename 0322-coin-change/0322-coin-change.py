class Solution:
    def __init__(self):
        self.cache = {}


    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        if amount in self.cache:
            return self.cache[amount]
        num = float('inf')
        for c in coins:
            currNum = self.coinChange(coins, amount - c)
            if currNum != -1 and 1 + currNum < num:
                num = 1 + currNum
        num = -1 if num == float('inf') else num
        self.cache[amount] = num
        return num
    
        