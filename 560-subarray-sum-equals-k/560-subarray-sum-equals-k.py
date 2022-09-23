class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {}
        count = 0
        m[nums[0]] = 1
        runningSum = nums[0]
        if(runningSum == k):
            count += 1
        for index in range(1, len(nums)):
            runningSum += nums[index]
            if(runningSum == k):
                count += 1
            count += m[runningSum-k] if runningSum -k in m else 0
            m[runningSum] = m[runningSum]+ 1 if runningSum in m else 1
        return count