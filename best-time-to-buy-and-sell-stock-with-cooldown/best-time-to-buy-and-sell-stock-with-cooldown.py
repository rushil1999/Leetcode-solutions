class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 1):
            return 0
        size = len(prices)
        dp = [[0]*2 for _ in range(size)]
        
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        
        dp[1][0] = max(dp[0][0], -prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
        
        for i in range(2, size):
            dp[i][0] = max(dp[i-1][0], -prices[i], dp[i-2][1] -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            
        return (max(dp[size-1][0], dp[size-1][1]))
        # return 0