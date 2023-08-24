class Solution(object):
    def majorityElement(self, nums):
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


