class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #return self.combinationSumDP(candidates, target)
        return self.combinationSumBackTrack(candidates, target)

    def combinationSumDP(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(len(candidates) + 1)]
        for c in candidates:
            for i in range(c, target+1):
                for comb in dp[i-c]:
                    newComb = list(comb)
                    newComb.append(c)
                    dp[i].append(newComb)
        return dp[target]


    def combinationSumBackTrack(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
        
        backtrack(target, [], 0)

        return results
        