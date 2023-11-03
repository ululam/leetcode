class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums)-1
        curr = 0
        while curr <= high:
            if nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                low += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
            else:
                curr += 1

                