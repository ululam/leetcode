class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length < 3) {
            return nums[0];
        }
        
        Integer candidate = null;
        int sum = 0;
        for (int n : nums) {
            if (sum == 0) {
                candidate = n;
            }
            
            sum += n == candidate ? 1 : -1;
        }
        
        return candidate;
    }
}