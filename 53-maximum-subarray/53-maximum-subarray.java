class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = currentSum;
        for (int i = 1; i<nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
            //System.out.printf("i = %s, cs = %s, maxs = %s\n", i, currentSum, maxSum);
        }
        
        return maxSum;
    }
}