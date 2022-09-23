class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for a in range(1, amount+1):
            for j in coins:
                if(a >= j):
                    dp[a] = min(dp[a], dp[a-j]+1)
        return -1 if dp[amount] > amount  else dp[amount]