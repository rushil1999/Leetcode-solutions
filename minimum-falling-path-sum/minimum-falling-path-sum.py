class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memo = {}
        def recurse(i,j):
            if(i<0 or j <0 or j>=m):
                return float('inf')
            if((i,j) in memo):
                return memo[(i,j)]
            topLeft = recurse(i-1, j-1)
            top = recurse(i-1, j)
            topRight = recurse(i-1, j+1)
            
            val = min(topLeft, top, topRight)
            if(val == float('inf')):
                val = 0
            memo[(i,j)] = val+ matrix[i][j]
            return memo[(i,j)]
    
        minVal = float('inf')
        for i in range(m):
            minVal = min(minVal, recurse(n-1, i))
        return minVal