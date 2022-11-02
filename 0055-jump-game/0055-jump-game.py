class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = []
        dp.append([0,nums[0]])
        for index in range(1, len(nums)):
            stepsTaken = max(dp[index-1][0], dp[index-1][1])-1
            stepsAvailable = nums[index] if stepsTaken >= 0 else 0
            dp.append([ stepsTaken, stepsAvailable])
        return True if dp[-1][0]>=0 else False