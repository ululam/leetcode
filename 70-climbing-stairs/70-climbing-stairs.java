class Solution {
    
    private int[] calculated = new int[45];
    {
        calculated[0] = 1;
        calculated[1] = 2;
        calculated[2] = 3;
    }
    
    public int climbStairs(int n) {
        if (calculated[n-1] == 0) {
            calculated[n-1] = climbStairs(n - 1) + climbStairs(n - 2);
        }
        
        return calculated[n-1];
    }
}