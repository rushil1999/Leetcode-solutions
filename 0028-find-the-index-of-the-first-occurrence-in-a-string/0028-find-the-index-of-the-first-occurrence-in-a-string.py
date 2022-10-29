class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index in range(len(haystack)):
            if(haystack[index] == needle[0]):
                if(index + len(needle)-1 < len(haystack)):
                    if(haystack[index: index+len(needle)] == needle):
                        return index
        return -1