class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def bt(remain, comb, start):
            if remain < 0:
                return
            if remain == 0:
                results.append(list(comb))
                return

            for i in range(start, len(candidates)):
                n = candidates[i]
                comb.append(n)
                bt(remain-n, comb, i)
                comb.pop()

        bt(target, [], 0)
        return results