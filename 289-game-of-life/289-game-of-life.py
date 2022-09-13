class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        changes = []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                neighbours = [0]*2
                if(i-1>=0 and j-1>=0):
                    neighbours[board[i-1][j-1]]+= 1
                if(i-1>=0):
                    neighbours[board[i-1][j]]+= 1
                if(j-1>=0):
                    neighbours[board[i][j-1]]+= 1
                if(i-1>=0 and j+1<cols):
                    neighbours[board[i-1][j+1]]+= 1
                if(j+1< cols):
                    neighbours[board[i][j+1]]+= 1
                if(i+1<rows and j+1<cols):
                    neighbours[board[i+1][j+1]]+= 1
                if(i+1<rows and j-1>=0):
                    neighbours[board[i+1][j-1]]+= 1
                if(i+1<rows):
                    neighbours[board[i+1][j]]+= 1
                
                if(neighbours[1] < 2 and board[i][j] == 1):
                    changes.append((i,j))
                elif(board[i][j] ==1 and (neighbours[1] == 2 or neighbours[1] == 3) ):
                    continue
                elif(board[i][j] == 1 and neighbours[1]>3):
                    changes.append((i,j))
                elif(board[i][j] == 0 and neighbours[1] == 3):
                    changes.append((i,j))
            
        for change in changes:
            row = change[0]
            col = change[1]
            board[row][col] = (board[row][col]+1)%2
        