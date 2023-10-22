class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high-low)>>1)
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:    # "<=" important to cope with situation when mid = 0
                # Left subarray
                if target < nums[mid] and target >= nums[0]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right subarray
                if target > nums[mid] and target <= nums[-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1