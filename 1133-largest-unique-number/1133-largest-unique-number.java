class Solution {
    public int largestUniqueNumber(int[] A) {
        if (A.length == 1) {
            return A[0];
        }
        
        if (A.length == 2) {
            return Math.max(A[0], A[1]);
        }
        
        Set<Integer> values = new HashSet<>(A.length/2);
        Set<Integer> duplicates = new HashSet<>(2);
        for (int i : A) {
            if (values.contains(i)) {
                duplicates.add(i);
            } else {
                values.add(i);
            }
        }

        int maxI = -1;
        for (int i : A) {
            if (i > maxI && ! duplicates.contains(i) ) {
                maxI = i;
            }
        }

        return maxI;
    }
}