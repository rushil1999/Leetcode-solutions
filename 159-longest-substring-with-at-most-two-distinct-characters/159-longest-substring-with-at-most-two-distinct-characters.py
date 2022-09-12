class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0,0
        res = 0
        countMap = {}
        
        while(right < len(s)):
            if(len(countMap) == 2):
                if(s[right] not in countMap):
                    keys = list(countMap.keys())
                    if(countMap[keys[0]] <= countMap[keys[1]]):
                        leftIncrement = countMap[keys[0]] + 1
                        del countMap[keys[0]]
                        countMap[s[right]] = right
                    else:
                        leftIncrement = countMap[keys[1]] + 1
                        del countMap[keys[1]]
                    left = leftIncrement
                    
            countMap[s[right]] = right
            # print(left, right, right-left+1, countMap)
            res = max(res, right-left+1)
            right += 1
        return res
                    