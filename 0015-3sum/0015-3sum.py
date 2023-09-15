class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #self.threeSumSorted(nums)
        return self.threeSumUnsorted(nums)

    def threeSumUnsorted(self, nums: List[int]) -> List[List[int]]:
        res, duplicates = set(), set()
        seen = {}
        for i, val in enumerate(nums):
            if val not in duplicates:
                duplicates.add(val)
                for j, valj in enumerate(nums[i+1:]):
                    summa = - (val + valj)
                    if seen.get(summa) == i: # We saw that value in the current extermal loop
                        res.add(tuple(sorted((val, valj, summa))))
                    seen[valj] = i
        return res


    def threeSumSorted(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        n = nums[i]
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            summa = nums[lo] + nums[hi]
            if summa < -n:
                lo += 1
            elif summa > -n:
                hi -= 1
            else:
                res += [[n, nums[lo], nums[hi]]]
                lo += 1
                hi -= 1
                while lo < hi and nums[lo-1] == nums[lo]:
                    lo += 1

