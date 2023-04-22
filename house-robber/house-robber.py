class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [[0] *2 for _ in range(size)]
        print(dp)
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[size-1][0], dp[size-1][1])