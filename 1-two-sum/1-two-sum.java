class Solution {
    public int[] twoSum(int[] nums, int target) {
        final Map<Integer, Integer> prevNumsSet = new HashMap<>();
        for (int i=0; i< nums.length; i++) {
            // if (nums[i] > target) {
            //     continue;
            // }
            if (prevNumsSet.containsKey(nums[i])) {
                return new int[] {prevNumsSet.get(nums[i]), i};
            }   
        
            prevNumsSet.put(target - nums[i], i);
        }
        
        return null;
    }
}