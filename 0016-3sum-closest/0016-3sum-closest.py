class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        min_diff = float('inf')
        lenth = len(nums)
        for i in range(lenth):
            lo, hi = i+1, lenth - 1
            while lo < hi:
                summa = nums[i] + nums[lo] + nums[hi]
                if abs(target - summa) < abs(min_diff):
                    min_diff = target - summa
                if summa < target:
                    lo += 1
                elif summa > target:
                    hi -=1
                else:
                    break
        return target - min_diff
