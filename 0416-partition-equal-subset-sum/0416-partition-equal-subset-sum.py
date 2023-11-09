class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summa = sum(nums)
        if summa & 1 == 1: # Odd summa
            return False
        
        @cache
        def dfs(n, subSum) -> bool:
            if subSum == 0:
                return True
            if n == 0 or subSum < 0:
                return False
            return dfs(n-1, subSum - nums[n-1]) or dfs(n-1, subSum)

        return dfs(len(nums) - 1, summa >> 1)