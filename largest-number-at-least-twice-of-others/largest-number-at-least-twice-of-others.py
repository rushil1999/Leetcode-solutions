class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        currentMax = nums[0]
        index = 0
        found = True
        for i in range(1, len(nums)):
            if(nums[i] > currentMax):
                
                if(2*currentMax > nums[i]):
                    print("Here 1", nums[i], currentMax)
                    
                    found = False
                else:
                    found = True
                    index = i
                currentMax = nums[i]
                
            elif(2*nums[i] > currentMax):
                print("Here 2")
                found = False
        if(found == True):
            return index
        else:
            return -1