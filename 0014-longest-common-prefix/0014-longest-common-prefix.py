class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        minVal = float('inf')
        for s in strs:
            minVal = min(minVal, len(s))
        for i in range(minVal):
            tempSet = set([])
            for j in strs:
                tempSet.add(j[i])
            if(len(tempSet) > 1):
                break
            else:
                prefix = prefix + tempSet.pop()
        return prefix
