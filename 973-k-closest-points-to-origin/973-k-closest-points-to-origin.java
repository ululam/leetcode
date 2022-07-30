import java.util.Map.Entry;
//import java.util.stream.Stream;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, (a,b) -> dist(a) - dist(b));
        
        return Arrays.copyOf(points, k);
    }
    
    private int dist(int[] p) {
        return p[0]*p[0] + p[1]*p[1];
    }
}