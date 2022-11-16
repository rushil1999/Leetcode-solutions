class Solution:
    
    
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def traverseIsland(i,j):
            print(i,j)
            grid[i][j] = "0"
            if(i+1 < rows  and grid[i+1][j] == "1"):
                print("R1", i+1, j, grid[i+1][j])
                traverseIsland(i+1, j)
            if(i-1>=0  and grid[i-1][j] == "1"):
                print("R2", i-1, j, grid[i-1][j])
                traverseIsland(i-1, j)
            if(j+1 < cols  and grid[i][j+1] == "1"):
                print("R3", i, j+1, grid[i][j+1])
                traverseIsland(i, j+1)
            if(j-1 >=0  and grid[i][j-1] == "1"):
                print("R4", i, j-1, grid[i][j-1])
                traverseIsland(i, j-1)
        
        
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                # print(i,j, visited[i][j])
                if( grid[i][j] == "1"):
                    print("Inside")
                    traverseIsland(i,j)
                    count += 1
        return count