class Solution:
    # bit manipulation
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final = []
        for i in range(2**n, 2**(n+1)):
            temp = []
            bitStr = bin(i)[3:]
            for index in range(len(bitStr)):
                if(bitStr[index] == "1"):
                    temp.append(nums[index])
            final.append(temp)
        return final