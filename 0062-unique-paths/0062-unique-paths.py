class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         memo = {}
#         def helper(m,n):
#             if((m,n) in memo):
#                 return memo[(m,n)]
#             if(m == 1 and n == 1):
#                 return 1
#             if(m < 1 or n < 1):
#                 return 0
#             paths = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
#             memo[(m,n)] = paths
#             return paths 
#         return helper(m,n)

    def uniquePaths(self, m: int,n :int ) -> int:
        dp = [[1]*n for num in range(m)]
        for i in range(1,m):
            for j in range(1,n):
               
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
                
                