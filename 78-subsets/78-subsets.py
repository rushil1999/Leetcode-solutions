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
        final = []
        for num in nums:
            aux = []
            for element in final:
                temp = element[:]
                temp.append(num)
                aux.append(temp)
            final = final+ aux
            final.append([num])
        
        final.append([])
        return final