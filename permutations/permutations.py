class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        if(len(nums) == 1):
            return [nums]
        for index in range(len(nums)):
            newNums = nums[0:index] + nums[index+1: len(nums)]
            nextSetPermutations = self.permute(newNums)
            for i in range(len(nextSetPermutations)):
                nextSetPermutations[i] = [nums[index]] + nextSetPermutations[i] 
            final += nextSetPermutations
        return final