class Solution {
    public boolean containsDuplicate(int[] nums) {
        final Set<Integer> numbersSeen = new HashSet<>(nums.length);
        for (int i : nums) {
            if (numbersSeen.contains(i)) {
                return true;
            }
            numbersSeen.add(i);
        }
        
        return false;
    }
}