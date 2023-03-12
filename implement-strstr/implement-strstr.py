class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLength = len(needle)
        hLength = len(haystack)
        for i in range(len(haystack)):
            if(haystack[i] == needle[0]):
                if((i+nLength-1) < hLength and haystack[i:i+nLength] == needle):
                    return i
        return -1