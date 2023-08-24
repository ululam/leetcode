class Solution(object):
    def majorityElementOnMem(self, nums):
        # [1,2,3,4,4,4,4] => 4
        # [1] => 1
        # [1,2,1] => 1
        # [1,1,4,4,1,1,4,4,4] => 4
        counts = {}
        threshold = (len(nums) >> 1)
        for n in nums:
            nCount = counts.get(n, 0) + 1
            if nCount > threshold:
                return n
            counts[n] = nCount
        return -1

    def majorityElement(self, nums):
        candidate = None
        candidateCount = 0
        for i in range(0, len(nums)):
            if candidateCount == 0:
               candidate = nums[i] 
            candidateCount += 1 if nums[i] == candidate else -1
            if candidateCount > len(nums) >> 1:
                break

        return candidate


