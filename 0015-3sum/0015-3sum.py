class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negSumMap = {}
        res = {}
 
        size = len(nums)
        for i in range(size):
            negSumMap[-nums[i]] = i
       
        for i in range(size-1):
            for j in range(i+1, size):
                summa = nums[i] + nums[j]
                if summa in negSumMap and i != negSumMap[summa] and j != negSumMap[summa]:
                    v = [nums[i], nums[j], -summa]
                    key = ",".join([str(n) for n in sorted(v)])
                    if not key in res:
                        res[key] = v

        return res.values()