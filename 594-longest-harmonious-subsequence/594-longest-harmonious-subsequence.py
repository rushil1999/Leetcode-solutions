class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        
        for num in nums:
            freq[num] = 1 if num not in freq else freq[num]+1
        
        maxLength = 0
        for num in freq:
            val = 0
            if(num-1 in freq):
                val = freq[num-1] + freq[num]
                if(maxLength < val):
                    maxLength = val
            if(num+1 in freq):
                val = freq[num+1] + freq[num]
                if(maxLength < val):
                    maxLength = val
        return maxLength