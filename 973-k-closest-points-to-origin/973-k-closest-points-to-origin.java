

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        if (k == points.length) {
            return points;
        }
        if (k == 0) {
            return new int[0][0];
        }
        return quickSelect(points, k);
    }
    
    private int[][] quickSelect(int[][] points, int k) {
        int left = 0; 
        int right = points.length - 1;
        int pivotIndex;
        while ((pivotIndex = partition(points, left, right)) != k) {
            if (pivotIndex < k) {
                left = pivotIndex;
            } else {
                right = pivotIndex - 1;
            }
        }
        
        return Arrays.copyOf(points, k);
    }

    private int partition(int[][] points, int left, int right) {
        final int pivotIndex = choosePivot(left, right);
        final int pivotDist = dist(points[pivotIndex]);
        while (left < right) {
            if (dist(points[left]) >= pivotDist) {
                swap(points, left, right);
                right--;
            } else {
                left++;
            }
        }
        
        if (dist(points[left]) < pivotDist) 
            left++;
        
        return left;
    }

    private void swap(int[][] points, int left, int right) {
        int[] tmp = points[left];
        points[left] = points[right];
        points[right] = tmp;
    }
    
    private int choosePivot(int left, int right) {
        return (left + right)/2;
    }
    
    private int dist(int[] p) {
        return p[0]*p[0] + p[1]*p[1];
    }
}