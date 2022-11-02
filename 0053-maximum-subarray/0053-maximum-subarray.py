class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pointer = 0
        maxSum = nums[pointer]
        currentSum = nums[pointer]
        while(pointer < len(nums)):
            maxSum = max(maxSum, currentSum)
            i = len(nums)-1
            for i in range(pointer+1, len(nums)):
                # print(pointer, i, nums[i], currentSum)
                if(currentSum + nums[i] < nums[i]):
                    maxSum = max(maxSum, currentSum)
                    currentSum = nums[i]
                    pointer = i
                    break
                else:
                    currentSum += nums[i]
                    maxSum = max(maxSum, currentSum)

            if(i == len(nums)-1):
                maxSum = max(maxSum, currentSum)
                break
        return maxSum