class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0,0
        res = 0
        countMap = {}
        
        while(right < len(s)):
            if(len(countMap) == 2):
                if(s[right] not in countMap):
                    index = min(countMap.values())
                    leftIncrement = index + 1
                    del countMap[s[index]]
                    left = leftIncrement
                    
            countMap[s[right]] = right
            # print(left, right, right-left+1, countMap)
            res = max(res, right-left+1)
            right += 1
        return res
                    