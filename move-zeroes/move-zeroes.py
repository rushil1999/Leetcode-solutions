class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0,0
        while(i<len(nums) and j<len(nums)):
            if(nums[i] == 0):
                for j in range(j, len(nums)):
                    if(nums[j]!=0):
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
            
            i+= 1
            if(j<i):
                j = i
