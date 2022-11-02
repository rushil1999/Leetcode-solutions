class Solution:
    # bottom up approach
    # def canJump(self, nums: List[int]) -> bool:
    #     dp = []
    #     dp.append([0,nums[0]])
    #     for index in range(1, len(nums)):
    #         stepsTaken = max(dp[index-1][0], dp[index-1][1])-1
    #         stepsAvailable = nums[index] if stepsTaken >= 0 else 0
    #         dp.append([ stepsTaken, stepsAvailable])
    #     return True if dp[-1][0]>=0 else False
    
    
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for index in range(last, -1, -1):
            if(nums[index] + index >= last):
                last = index
        return last == 0