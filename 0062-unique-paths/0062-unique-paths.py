class Solution:
    # Top Down
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    
    
    # Bottom Up Recurssive
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         memo = {}
        
#         def helper(m,n):
#             if((m,n) in memo):
#                 return memo[(m,n)]
#             if(m < 1 or n < 1):
#                 return 0
#             if(m == 1 and n == 1):
#                 return 1
#             # target = (m-1, n-1)
#             top = self.uniquePaths(m-1, n)
#             left = self.uniquePaths(m, n-1)
#             memo[(m,n)] = top+left
#             return top+left
        
#         return helper(m,n)