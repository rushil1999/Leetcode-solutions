class Solution:
    def __init__(self):
        self.map = {}
    def issubsequence(self, s1, s2):
 
        n,m = len(s1),len(s2)
        i,j = 0,0
        while (i < n and j < m):
            if (s1[i] == s2[j]):
                i += 1
            j += 1
        self.map[s1] = True
        return i == n
    
    def shortestWay(self, source: str, target: str) -> int:
        dp1 = [0]*len(target)
        dp2 = [0]*len(target)
        if(target[0] in source):
            dp1[0] = 1
            dp2[0] = target[0]
        else:
            return -1
        for index in range(1,len(target)):
            if (target[index] not in source):
                return -1
            substr = dp2[index-1] + target[index]
            if(substr in self.map):
                dp1[index] = dp1[index-1]
                dp2[index] = substr
            if(self.issubsequence(substr, source) == True):
                dp1[index] = dp1[index-1]
                dp2[index] = substr
            else:
                dp1[index] = dp1[index-1]+1
                dp2[index] = target[index]
        return dp1[len(target)-1]