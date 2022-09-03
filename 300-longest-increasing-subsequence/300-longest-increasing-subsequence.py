class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(0, len(nums)):
            for j in range(i-1, -1, -1):
                if(nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)