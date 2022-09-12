class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0,0
        res = 0
        countMap = {}
        if(k == 0):
            return 0
        while(right < len(s)):
            if(len(countMap) == k):
                if(s[right] not in countMap):
                    index = min(countMap.values())
                    left = index + 1
                    del countMap[s[index]]
                
            countMap[s[right]] = right
            res = max(res, right-left+1)
            right += 1
        return res
        