class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        countMap = {}
        while(right < len(s)):
            if(s[right] in countMap):
                left = countMap[s[right]]+1 if countMap[s[right]]+1 > left else left
            countMap[s[right]] = right
            
            # print(left, right, countMap, right-left+1)
            res = max(res, right-left+1)
            right+= 1
        return res
            