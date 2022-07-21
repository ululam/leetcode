class Solution {
    public static final int STR=0;
    public static final int END=1;
    
    public int[][] insert(int[][] intervals, int[] newin) {
        List<int[]> result = new ArrayList<>();
        for(int[] in : intervals) {
            if(newin[END]<in[STR]) {
               result.add(newin);
               newin = in ; 
            } else if(in[END] < newin[STR]) {
               result.add(in); 
            } else {
               newin[STR] = Math.min(newin[STR],in[STR]) ; 
               newin[END] = Math.max(newin[END],in[END]) ; 
            }
        }
        result.add(newin);
        return result.toArray(new int[result.size()][2]);
    }
}