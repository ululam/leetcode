class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high-low)>>1)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1