class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        k,K = i+1, len(nums) - 1
        while k < K:
            summa = nums[k] + nums[K]
            if summa < -nums[i]:
                k += 1
            elif summa > -nums[i]:
                K -= 1
            else:
                res.append([nums[i], nums[k], nums[K]])
                k += 1
                K -= 1
                while nums[k-1] == nums[k] and k < K:
                    k += 1