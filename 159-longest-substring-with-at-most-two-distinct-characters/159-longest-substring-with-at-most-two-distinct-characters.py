class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0,0
        res = 0
        countMap = {}
        
        while(right < len(s)):
            if(len(countMap) == 2):
                if(s[right] not in countMap):
                    index = min(countMap.values())
                    left = index + 1
                    del countMap[s[index]]                    
            countMap[s[right]] = right
            res = max(res, right-left+1)
            right += 1
        return res
                    