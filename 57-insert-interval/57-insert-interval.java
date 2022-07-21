class Solution {
    public int[][] insert(int[][] intervals, int[] newin) {
        List<int[]> result = new ArrayList<>();
        for(int[] in : intervals) {
            if(newin[1]<in[0]) {
               result.add(newin);
               newin = in ; 
            } else if(in[1] < newin[0]) {
               result.add(in); 
            } else {
               newin[0] = Math.min(newin[0],in[0]) ; 
               newin[1] = Math.max(newin[1],in[1]) ; 
            }
        }
        result.add(newin);
        return result.toArray(new int[result.size()][2]);
    }
}