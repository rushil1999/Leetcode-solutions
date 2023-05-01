class Solution:
    
    def getMinAndSecondMin(self, arr: List[int]):
        size = len(arr)
        minIndex, minIndex2 = 0,0
        
        val = float('inf')
        for i in range(size):
            if(arr[i]  <=val):
                val = arr[i]
                minIndex = i
                
        val2 = float('inf')
        
        for i in range(size):
            if(arr[i] <= val2 and arr[i] >= val and minIndex != i):
                val2 = arr[i]
                minIndex2 = i
        return [minIndex, minIndex2]
        
    def minCostII(self, costs: List[List[int]]) -> int:
        size = len(costs)
        k = len(costs[0])
        dp = [[0]*k for _ in range(size) ]
        minIndex = [float('inf') for _ in range(size)]
        minIndex2 = [float('inf') for _ in range(size)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        [minimumIndex, minimumIndex2] = self.getMinAndSecondMin(dp[0])
        minIndex[0] = minimumIndex
        minIndex2[0] = minimumIndex2
            
            
        for i in range(1, size):
            for j in range(k):
                if(minIndex[i-1] == j):
                    dp[i][j] = dp[i-1][minIndex2[i-1]] + costs[i][j]
                else:
                    dp[i][j] = dp[i-1][minIndex[i-1]] + costs[i][j]
                    
                [minimumIndex, minimumIndex2] = self.getMinAndSecondMin(dp[i])
                minIndex[i] = minimumIndex
                minIndex2[i] = minimumIndex2        
        return dp[size-1][minIndex[size-1]]