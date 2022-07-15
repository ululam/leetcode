class Solution {
    public int maxProfit(int[] prices) {
        // Take number
        // If next is larger, calc delta. If delta > cuurent delta, current = detla
        // If next is smaller, replace number
        // If same, do nothing
        if (prices.length < 2) {
            return 0;
        }
        
        int currentP = prices[0];
        int maxProfit = 0;
        
        for (int i = 1; i < prices.length; i++) {
            int p = prices[i];
            if (p >= currentP) {
                int profit = p - currentP;
                maxProfit = maxProfit > profit ? maxProfit : profit;
            } else {
                currentP = p;
            }
        }
        
        return maxProfit;
    }
}