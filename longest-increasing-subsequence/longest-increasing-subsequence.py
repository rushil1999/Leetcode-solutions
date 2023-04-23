class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size
        maxVal = 1
        for i in range(1, size):
            for j in range(0, i):
                if(nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j]+1)
                    maxVal = max(maxVal, dp[i])
        return maxVal