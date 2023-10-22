class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high-low)>>1)
            print(f"\t [{low},{high}] -> {mid} ")
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
            # if nums[mid] >= nums[0]:
            #     if target >= nums[low] and target < nums[mid]:
            #         high = mid-1
            #     else:
            #         low = mid + 1
            # else:
            #     if target <= nums[-1] and target > nums[mid]:
            #         low = mid + 1
            #     else:
            #         high = mid - 1
        return -1