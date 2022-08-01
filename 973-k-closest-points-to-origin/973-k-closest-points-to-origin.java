import java.util.Map.Entry;
//import java.util.stream.Stream;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        return quickSelect(points, k);
    }
    
    private int[][] quickSelect(int[][] points, int k) {
        int left = 0;
        int right = points.length - 1;
        int pivotIndex = points.length;
        while (pivotIndex != k) {
            pivotIndex = partition(points, left, right);
            if (pivotIndex < k) {
                left = pivotIndex;
            } else {
                right = pivotIndex - 1;
            }
        }
        
        return Arrays.copyOf(points, k);
    }    
    
    private int partition(int[][] points, int left, int right) {
        final int pivotIndex = selectPivot(left, right);
        final int[] pivotPoint = points[pivotIndex];
        final int pivotDist = dist(pivotPoint);
        
        while (left < right) {
            if (dist(points[left]) >= pivotDist) {
                swap(points, left, right);
                right--;
            } else {
                left++;
            }
        }
        
        // Should break through pivot
        if (dist(points[left]) < pivotDist) left++;
        
        return left;
    }
    
    private void swap(int[][] points, int left, int right) {
        int[] tmp = points[left];
        points[left] = points[right];
        points[right] = tmp;
    }
    
    private int selectPivot(int left, int right) {
        return (left + right) / 2;
    }
    
    private int dist(int[] p) {
        return p[0]*p[0] + p[1]*p[1];
    }
}