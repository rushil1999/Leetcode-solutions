class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        
        topRow = False
        leftCol= False
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == 0):
                    if(i == 0):
                        topRow = True
                    if(j==0):
                        leftCol = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        print(matrix)
        for i in range(1,n):
            for j in range(1,m):
                # print(i,j, matrix[i][0], matrix[0][j])
                if(matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
                    
        print(matrix)
        
        
#         for j in range(m):
#             if(matrix[0][j] == 0):
#                 topRow = True
                
                
#         for i in range(n):
#             if(matrix[i][0] == 0):
#                 leftCol = True
                
        if(topRow == True):
            for j in range(m):
                matrix[0][j] = 0

                
        if(leftCol == True):
            for i in range(n):
                matrix[i][0] = 0

        
            
                
        
            
                    