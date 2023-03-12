class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0 for _ in range(len(nums))]
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] += prefixSum[i-1]+nums[i]
        print(prefixSum)
        totalSum = prefixSum[-1]
        for i in range(len(nums)):
            if(prefixSum[i] - nums[i] == totalSum - prefixSum[i]):
                return i
        return -1