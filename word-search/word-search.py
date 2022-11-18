class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(board)
        m = len(board[0])
        visited = [[False]*m for _ in range(n)]
        def helper(i,j,ptr):
            # print(board[i][j])
            if(ptr == len(word)-1 and board[i][j] == word[ptr]):
                return True
            if(board[i][j] != word[ptr]):
                return False
            
            
            visited[i][j] = True
            val = False
            count = 0
            while(count < 1):
                if(i+1 < n and visited[i+1][j] == False):
                    val = helper(i+1, j, ptr+1)
                    if(val == True):
                        break
                if(i-1 >= 0 and visited[i-1][j] == False):
                    val = helper(i-1, j, ptr+1)
                    if(val == True):
                        break
                if(j+1 < m and visited[i][j+1] == False):
                    val = helper(i, j+1, ptr+1)
                    if(val == True):
                        break
                if(j-1 >=0 and visited[i][j-1] == False ):
                    val = helper(i, j-1, ptr+1)
                    if(val == True):
                        break
                count += 1
            
            visited[i][j] = False
            # print(board[i][j], val)
            return val
    
        for i in range(n):
            for j in range(m):
                if(board[i][j] == word[0]):
                    val = helper(i,j,0)
                    if(val == True):
                        return True
            
        return False