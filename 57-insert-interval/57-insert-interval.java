class Solution {
    private static final int START = 0;
    private static final int END = 1;
    
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new LinkedList<>();
        int[] newin = newInterval;
        for (int[] in : intervals) {
            if (in[END] < newin[START]) {
                res.add(in);
            } else if (in[START] > newin[END]) {
                res.add(newin);
                newin = in;
            } else {
                newin[START] = Math.min(in[START], newin[START]);
                newin[END] = Math.max(in[END], newin[END]);
            }
        }
        
        res.add(newin);
        return res.toArray(new int[res.size()][2]);
    }
}