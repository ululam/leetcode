class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            return new int[][] {newInterval};
        }
        List<int[]> intervalList = new ArrayList<>(Arrays.asList(intervals));
        
        int startPos = -1;
        int endPos = -1;
        for (int i=0;i<intervals.length;i++) {
            if (startPos < 0) {
                if (intervals[i][0] > newInterval[1]) {
                    intervalList.add(i, newInterval);

                    return intervalList.toArray(new int[intervalList.size()][2]);
                }    
                if (intervals[i][0] >= newInterval[0]) {
                    startPos = i;
                } else if (intervals[i][1] >= newInterval[0]) {
                    newInterval[0] = intervals[i][0];
                    startPos = i;
                }
            }
            
            if (startPos >= 0) {
                if (intervals[i][0] > newInterval[1]) {
                    break;
                } else {
                    endPos = i;
                    if (intervals[i][1] >= newInterval[1]) {
                        newInterval[1] = intervals[i][1];
                        break;
                    }
                }
            }
        }
        
        
//         p("Resulting new interval: [%s,%s]", newInterval[0], newInterval[1]);
//         p("start pos is %s", startPos);
//         p("end pos is %s", endPos);
        
//         p("Before removal, list is: [%s]", intervalList.stream().map(Arrays::toString).collect(Collectors.joining(",")));

        if (startPos >= 0) {
            if (endPos < 0) endPos = startPos;

            for (int i=endPos;i>=startPos;i--) {
                intervalList.remove(i);
            }
        } else {
            startPos = intervals.length;
        }
        
        // p("After removal, list is: [%s]", intervalList.stream().map(Arrays::toString).collect(Collectors.joining(",")));
        
        intervalList.add(startPos, newInterval);
        
        return intervalList.toArray(new int[intervalList.size()][2]);
    }
    
    private static void p(String s, Object... vals) {
        //System.out.printf(s+"\n", vals);
    }
}