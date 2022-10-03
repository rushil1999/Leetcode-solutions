class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dp = []
        for num in range(1, n+1):
            dp.append(num)
        # print(dp)
        index = 0
        while(len(dp) > 1):
            index = ((index+k-1)%len(dp))
            # print("Iteration", index)
            # print("Plaer leaving the game", index, dp[index])
            dp = dp[0:index]+dp[index+1:len(dp)]
            # index += 1
            # print("After Removal", dp, index)
        return dp[0]