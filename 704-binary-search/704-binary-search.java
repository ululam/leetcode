class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int i;
        while (left <= right) {
            i = left + ((right-left) >> 1);
            if (nums[i] == target) {
                return i;
            }
            if (nums[i] > target) {
                right = i - 1;
            } else {
                left = i + 1;
            }
        }
        
        return -1;
    }    
}