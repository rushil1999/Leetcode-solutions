class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [[0]*2 for _ in range(size+1)]
        if(len(cost) == 1):
            return cost[0]
        if(len(cost) == 2):
            return min(cost[0], cost[1])
        dp[0][0], dp[0][1] = 0,0
        dp[1][0] = cost[0]
        dp[1][1] = 0
        
        for i in range(2, size+1):
            dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + cost[i-1]
            dp[i][1] = min(dp[i-2][0], dp[i-2][1]) + cost[i-2]
        val = min(dp[size][0], dp[size][1])
        return val