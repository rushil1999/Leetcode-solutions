class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        countMap = {}
        while(right < len(s)):
            countMap[s[right]] = 1 if s[right] not in countMap else countMap[s[right]]+1
            # print(right, left, s[right], countMap)

            while(countMap[s[right]]>1):
                countMap[s[left]] -= 1
                left += 1
            
            # print("Length ", right- left+1, right, left)
            res = max(res, right-left+1)
            right+= 1
        return res
            