class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        final Map<Integer, Integer> nums2inds = new HashMap<>(nums.length);
        for (int i=0; i<nums.length;i++) {
            nums2inds.put(nums[i], i);
        }
        
        Set<T3> res = new HashSet<>();
        for (int i=0; i<nums.length;i++) {
            for (int j=i+1; j<nums.length;j++) {
                int sum = -1 * (nums[i] + nums[j]);
                if (nums2inds.containsKey(sum)) {
                    int index = nums2inds.get(sum);
                    if (index != i && index != j) {
                        T3 t3 = new T3(new int[] {nums[i], nums[j], sum});
                        res.add(t3);
                    }
                }
            }
        }
        
        return res.stream().map(T3::toList).collect(Collectors.toList());
    }
}

class T3 {
    int a;
    int b;
    int c;
    
    T3(int[] vals) {
        Arrays.sort(vals);
        this.a = vals[0];
        this.b = vals[1];
        this.c = vals[2];
    }
    
    public boolean equals(Object o) {
        if (! (o instanceof T3)) return false;
        T3 t3 = (T3) o;
        return t3.a == this.a && t3.b == this.b && t3.c == this.c;
    }
    
    public int hashCode() {
        return 100*a + 10*b + c;
    }
    
    public List<Integer> toList() {
        return Arrays.asList(a,b,c);
    }
}