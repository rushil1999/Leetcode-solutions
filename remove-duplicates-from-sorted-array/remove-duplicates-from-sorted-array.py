class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i
        while(i < len(nums) and j <len(nums)):
            while(j<len(nums)):
                if(nums[j] != nums[i]):
                    i+= 1
                    nums[i] = nums[j]
                
                j+= 1
        return i+1