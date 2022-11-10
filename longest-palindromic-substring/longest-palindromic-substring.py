class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        # print(dp)
        
        for i in range(n):
            dp[i][i] = 1
        
        maxLength = 1
        maxIndices = (0,0)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i ==1 or dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                        if(j-i+1 >= maxLength):
                            maxLength = j-i+1
                            maxIndices = (i,j)
                
        # print(dp)
        return s[maxIndices[0]:maxIndices[1]+1]