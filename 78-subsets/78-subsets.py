class Solution:
    
    # def helper(self, nums):
    #     final = []
    #     if(len(nums) == 1):
    #         final.append([nums[0]])
    #         return final
    #     else:
    #         temp = self.helper(nums[0:len(nums)-1])
    #         final = temp[:]
    #         final.append([nums[len(nums)-1]])
    #         for element in temp:
    #             newElement = element[:]
    #             newElement.append(nums[len(nums)-1])
    #             final.append(newElement)
    #     return final
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final = []
        
        for i in range(2**n, 2**(n+1)):
            
            bitmask = bin(i)[3:]
            print(i,bitmask, bin(i))
            
            final.append([nums[j] for j in range(n) if bitmask[j] == '1']) 
        return final