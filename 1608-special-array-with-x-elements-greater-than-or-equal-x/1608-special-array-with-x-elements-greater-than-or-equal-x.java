class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums); // [1, 4, 7, 17, 22]
        // int special = nums[nums.length >> 1]; // [2] -> 7
        
        // N = nums.length >> 1; => 2 
        // el = nums[N]; => 7
        // 
        
        // 7 > (5-2) => step left
        // 
        // 1 < (5-2) => step right, delta = -2
        // 3 == (5-2) => return
        
        // while (special)
        
        for (int i = 0; i < nums.length; i++) {
            int special = nums.length - i;
            if (i > 0 && nums[i-1] >= special) {
                return -1;
            }
            if (nums[i] >= special) {
                return special;
            }
        }
        
        return -1;
        
    }
}