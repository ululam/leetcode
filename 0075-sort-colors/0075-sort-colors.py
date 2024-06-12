class Solution(object):
    def sortColors(self, nums):
        if not nums:
            return nums
        left, curr, right = 0, 0, len(nums) - 1
        while left < right and nums[left] == 0:
            left += 1
        curr = left
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
            if nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1

        return nums
        