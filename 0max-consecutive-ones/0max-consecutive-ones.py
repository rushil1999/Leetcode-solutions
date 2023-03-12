class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slow, fast = 0,0
        maxCount = 0
        while(slow < len(nums)):
            if(nums[slow] == 1):
                fast = slow
                currentCount = 0
                while(fast < len(nums) and nums[fast] == 1):
                    fast += 1
                    currentCount += 1
                slow = fast
                maxCount = max(maxCount, currentCount)
            slow += 1
        return maxCount