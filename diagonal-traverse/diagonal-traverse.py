class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        direction = "up"
        n,m = len(mat), len(mat[0])
        ans = []
        i,j = 0,0
        while(True):
            if(i > n or j > m or i<0 or j<0):
                break
            if(i == n-1 and j == m-1):
                ans.append(mat[i][j])
                break
            if(direction == "up"):
                while(i>=0 and j<m ):
                    print("Direction up", i, j, mat[i][j])
                    ans.append(mat[i][j])
                    i-=1
                    j+=1
                
                if(i<0 and j<m):
                    i=0
                if(i<0 and j>=m):
                    i=1
                    j=m-1
                if(i>=0 and j>=m):
                    i+=2
                    j = m-1
                direction = "down"
            if(direction == "down"):
                while(i<n and j>=0):
                    print("Direction Down", i, j, mat[i][j])
                    ans.append(mat[i][j])
                    i+=1
                    j-=1
                if(j<0 and i<n):
                    j=0
                if(j<0 and i>=n):
                    j=1
                    i=n-1
                if(j>=0 and i>=n):
                    j+=2
                    i = n-1
                    # print("caught", i, j)
                direction = "up"
            
                    
        return ans
                        