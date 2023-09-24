class Solution:
    def __init__(self):
        self.cache = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeBottomUp(coins, amount)

    def coinChangeBottomUp(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for am in range (1, amount + 1):
            for c in coins:
                if am - c >= 0:
                    dp[am] = min(dp[am], 1 + dp[am-c])
        return dp[amount] if dp[amount] <= amount else -1

    def coinChangeMem(self, coins: List[int], amount: int) -> int:
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
    
        