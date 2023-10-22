class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find pivot index O(logN)
        # Now we have 4 values min1, max1, min2, max2
        # Identify at which subarrat our target falls, and then do search again
        # O(2logN) = O(logN)
        if len(nums) < 4:
            for i, n in enumerate(nums):
                if n == target:
                    return i
            return -1
        
        pivot = self._findPivotIndex(nums)
        print(f"pivot = {pivot}")
        if pivot == -1:
            return self._search(nums, 0, len(nums)-1, target)
        print(f"intervals: (0,{pivot}), ({pivot+1},{len(nums)-1})")
        answer = self._search(nums, 0, pivot-1, target)
        if answer != -1:
            return answer
        return self._search(nums, pivot, len(nums)-1, target)

    def _findPivotIndex(self, nums):
        low, high = 0, len(nums) - 1
        # search for break point
        while low <= high:
            pivot = low + ((high-low)>>1)
            print(f"p = {pivot}")
            if nums[pivot] <= nums[-1]:
                high = pivot-1
            else:
                low = pivot+1
        return low
        

    def _search(self, nums, low, high, target):
        print(f"Searching {target} in [{low},{high}]")
        while low <= high:
            pivot = low + ((high-low)>>1)
            print(f"\t> [{low},{high}] -> p = {pivot}")
            if nums[pivot] > target:
                high = pivot-1
            elif nums[pivot] < target:
                low = pivot+1
            else:
                return pivot
        return -1
        