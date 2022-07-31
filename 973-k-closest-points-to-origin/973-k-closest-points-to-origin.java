import java.util.Map.Entry;
//import java.util.stream.Stream;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        final Queue<int[]> pQueue = new PriorityQueue<>((a,b) -> b[0] - a[0]);
        for (int i=0; i<points.length; i++) {
            int[] data = new int[] {dist(points[i]), i}; 
            if (pQueue.size() < k) {
                pQueue.add(data);
            } else if (pQueue.peek()[0] > data[0]) {
                pQueue.poll();
                pQueue.add(data);
            }
        }
        
        int[][] res = new int[k][2];
        int i = 0;
        while (!pQueue.isEmpty()) {
            int index = pQueue.poll()[1];
            res[i++] = points[index];
        }
            
        return res;
    }
    
    private int dist(int[] p) {
        return p[0]*p[0] + p[1]*p[1];
    }
    
}