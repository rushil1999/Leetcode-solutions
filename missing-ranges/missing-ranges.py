class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        final = []
        ans = []
        for index in range(1, len(nums)):
            if(nums[index] - nums[index-1] > 1):
                candidateRange = [nums[index-1]+1,nums[index]-1]
                # print(candidateRange)
                if(candidateRange[0] >= lower and candidateRange[0] <= upper):
                    intersection = [max(candidateRange[0], lower), min(candidateRange[1], upper)]
                    print(intersection)
                    final.append(intersection)
        
        if(len(nums)> 0 and nums[len(nums)-1] < upper):
            final.append([nums[len(nums)-1]+1, upper])
        if(len(nums)> 0 and nums[0] > lower):
            final =[[lower, nums[0]-1]]+ final
        elif(len(nums) == 0):
            final.append([lower, upper])
        print(final)
        for element in final:
            if(element[0] == element[1]):
                ans.append(str(element[0]))
            else:
                s = ""
                s += str(element[0])
                s += "->"
                s += str(element[1])
                ans.append(s)
        return ans