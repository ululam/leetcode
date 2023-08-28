class Solution(object):
  def maxSubArray(self, nums: List[int]) -> int:
    maxSum = currentSum = nums[0]

    for n in nums[1:]:
        # if we were sure there are positive numbers in array (at least 1),
        # we could od (if currentSum < 0) -- drop and start over using the next number.
        # But that's not true, and we still need to cope with data like [-2,-1,-3]
        # So we start over when the previous sum is less than the current element
        if currentSum + n < n:
            currentSum = n
        else:
            currentSum += n
        # or, we can write:
        # currentSum = max(nums[i], currentSum + nums[i])

        maxSum = max(maxSum, currentSum)

    return maxSum
