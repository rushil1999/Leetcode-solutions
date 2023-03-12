class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast = 0,0
        currentSum = 0
        minLength = len(nums)+1
        while(fast < len(nums)):
            currentSum += nums[fast]
            while(currentSum >= target):
                minLength = min(minLength, fast-slow+1)
                # print(minLength, slow, fast)
                if(minLength == 1):
                    return 1
                currentSum -= nums[slow]
                slow+= 1
            fast += 1
        
        return minLength if minLength <= len(nums) else 0
        