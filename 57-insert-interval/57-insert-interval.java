class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>(intervals.length + 1);
        int[] newin = newInterval;
        for (int[] in : intervals) {
            if (in[1] < newin[0]) {
                res.add(in);
            } else if (in[0] > newin[1]) {
                res.add(newin);
                newin = in;
            } else {
                newin[0] = Math.min(newin[0], in[0]);
                newin[1] = Math.max(newin[1], in[1]);
            }
        }
        
        res.add(newin);
        return res.toArray(new int[res.size()][2]);
    }
}