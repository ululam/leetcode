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
        candidateCount, othersCount = 0,0
        for i in range(0, len(nums)):
            if not candidate:
               candidate = nums[i] 
            if nums[i] == candidate:
                candidateCount += 1
                if candidateCount > len(nums) >> 1:
                    return candidate
            else:
                othersCount += 1
                if candidateCount == othersCount:
                    candidateCount = 0
                    othersCount = 0
                    candidate = None


        return candidate


