class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nu,s

        headMults = [0] * len(nums)
        headMults[0] = nums[0]
        tailMults = [0] * len(nums)
        tailMults[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            headMults[i] = headMults[i-1] * nums[i]
            revIndex = len(nums) - i - 1
            tailMults[revIndex] = tailMults[revIndex+1] * nums[revIndex]
        
        res = []
        res.append(tailMults[1])
        for i in range(1, len(nums)-1):
            res.append(headMults[i-1] * tailMults[i+1])
        res.append(headMults[len(nums) - 2])

        return res
