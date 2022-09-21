class Solution:
    
    def helper(self, nums):
        final = []
        if(len(nums) == 1):
            final.append([nums[0]])
            print("Initial",final)
            return final
        else:
            print("Before recurring", nums)
            temp = self.helper(nums[0:len(nums)-1])
            print("Nums",nums, temp)
            final = temp[:]
            final.append([nums[len(nums)-1]])
            for element in temp:
                print("Element",element)
                newElement = element[:]
                newElement.append(nums[len(nums)-1])
                print("New Element", newElement)
                final.append(newElement)
            print(final)
        return final
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = self.helper(nums)
        final.append([])
        
        return final