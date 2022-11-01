class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        startPoints = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        n = len(board)
        m = len(board[0])
        finalFlag = True
        for points in startPoints:
            boxSet = set([])
            boxCount = 0
            for i in range(points[0],points[0]+3):
                for j in range(points[1], points[1]+3):
                    if(board[i][j] != '.'):
                        boxSet.add(board[i][j])
                        boxCount += 1
            if(len(boxSet) != boxCount):
                print("Break 1")
                return False
        for i in range(n):
            rowCount = 0
            colCount = 0
            rowSet = set([])
            colSet = set([])
            for j in range(m):
                if(board[i][j] != '.'):
                    rowSet.add(board[i][j])
                    rowCount += 1
                    
                if(board[j][i] != '.'):
                    colSet.add(board[j][i])
                    colCount += 1
            if(len(rowSet) != rowCount or len(colSet) != colCount):
                print("Break 2", rowSet, rowCount, colSet, colCount)
                return False
        
        return True
            