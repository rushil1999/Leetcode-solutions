class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [[0]*m for _ in range(n)]
        
        obstacleTopRow = False
        for i in range(m):
            if(obstacleGrid[0][i] == 0 and obstacleTopRow == False):
                dp[0][i] = 1
            else: dp[0][i] = -1
            if(obstacleGrid[0][i] == 1):
                obstacleTopRow = True
        
        obstacleLeftCol = False
        for i in range(n):
            if(obstacleGrid[i][0] == 0 and obstacleLeftCol == False):
                dp[i][0] = 1
            else: dp[i][0] = -1
            if(obstacleGrid[i][0] == 1):
                obstacleLeftCol = True
                
        print(dp)
        for i in range(1,n):
            for j in range(1,m):
                print(i,j)
                if(obstacleGrid[i][j] == 1):
                    dp[i][j] = -1
                else:
                    val = 0

                    if(dp[i-1][j] > 0):
                        val += dp[i-1][j]
                    if(dp[i][j-1]>0):
                        val += dp[i][j-1]
                    dp[i][j] = val
        return dp[n-1][m-1] if dp[n-1][m-1] > 0 else 0
            