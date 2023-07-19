// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int result = 0;
        int minPrice = prices[0];
        for (int j = 1; j < n; ++j) {
            result = Math.max(result, prices[j] - minPrice);
            minPrice = Math.min(minPrice, prices[j]);
        }
        return result;
    }
}