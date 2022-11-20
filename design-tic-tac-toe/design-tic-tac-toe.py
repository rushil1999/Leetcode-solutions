class TicTacToe:

    def __init__(self, n: int):
        self.horizontal = [[0]*2 for _ in range(n)]
        self.vertical = [[0]*2 for _ in range(n)]
        self.diagonal1 = [0,0]
        self.diagonal2 = [0,0]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.horizontal[row][player-1] += 1
        self.vertical[col][player-1] += 1
        if(row == col):
            self.diagonal1[player-1] += 1
            if(self.diagonal1[0] == self.n):
                return 1
            elif(self.diagonal1[1] == self.n):
                return 2
        if(row+col == self.n-1):
            self.diagonal2[player-1]+=1
            if(self.diagonal2[0] == self.n):
                return 1
            if(self.diagonal2[1] == self.n):
                return 2
        if(self.horizontal[row][0] == self.n):
            return 1
        elif(self.horizontal[row][1] == self.n):
            return 2
        if(self.vertical[col][0] == self.n):
            return 1
        elif(self.vertical[col][1] == self.n):
            return 2
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)