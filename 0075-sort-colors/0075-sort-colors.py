class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Go through the array, if seen 0, swap with last non-0
        # If faced 2, do the same from the other end, and continue there
        # Until both pointers met

        low, high = 0, len(nums)-1
        curr = 0
        while curr <= high:
            if nums[curr] == 0:
                nums[low], nums[curr] = nums[curr], nums[low]
                low += 1
                curr += 1
            elif nums[curr] == 2:
                nums[high], nums[curr] = nums[curr], nums[high]
                high -= 1
            else:
                curr += 1
                