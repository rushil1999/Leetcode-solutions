class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 1):
            return [nums]
        permutations = []
        for index in range(0, len(nums)):
            newNums = nums[0:index] + nums[index+1:len(nums)]
            # print(nums[index], newNums)
            newNumsPermutations = self.permute(newNums)
            # print(nums[index], newNumsPermutations)
            for j in range(0, len(newNumsPermutations)):
                newNumsPermutations[j] = [nums[index]]+newNumsPermutations[j]
            permutations += newNumsPermutations
        return permutations
                