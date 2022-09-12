class Solution:
    def countDistinct(self, s: str) -> int:
        substringSet = set()
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                st = s[i:j]
                # print(st)
                substringSet.add(st)
        return len(substringSet)
        

