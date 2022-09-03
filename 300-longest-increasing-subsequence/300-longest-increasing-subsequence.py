class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(0, len(nums)):
            # print(i,nums[i])
            for j in range(i-1, -1, -1):
                # print("J", j)
                if(nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j]+1)
        # print(dp)
        return max(dp)