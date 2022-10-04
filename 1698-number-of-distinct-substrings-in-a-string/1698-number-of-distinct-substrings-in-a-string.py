class Solution:
    def countDistinct(self, s: str) -> int:
        # substringSet = set()
        m = set([])
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                st = s[i:j]
                # print(st)
                if(st not in m):
                    m.add(st)
        return len(m)
        

