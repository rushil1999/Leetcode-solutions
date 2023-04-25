class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
       
        n = len(grid)
        m = len(grid[0])
        memo = {}
        def recurse(i,j):
            if(i<0 or j<0):
                return float('inf')
            if((i,j) in memo):
                return memo[(i,j)]
            left = recurse(i, j-1)
            right = recurse(i-1,j)
            
            val = min(left, right)
            if(val == float('inf')):
                val = 0
            memo[(i,j)] = val + grid[i][j]
            return memo[(i,j)]
        return recurse(n-1, m-1)
        
        
        
        # Bottom-up approach
#         n = len(grid)
#         m = len(grid[0])
#         dp = [[0]*m for _ in range(n)]
#         dp[0][0] = grid[0][0]
#         for i in range(1,m):
#             dp[0][i] += dp[0][i-1]+grid[0][i]

#         for i in range(1,n):
#             dp[i][0] += dp[i-1][0]+grid[i][0]
            
            
#         for i in range(1, n):
#             for j in range(1, m):
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

#         return dp[n-1][m-1]
         
            
            
        