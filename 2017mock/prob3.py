class chess:
    def __init__(self):
        self.board = []
        self.board += [[2,0,0,0,6,0,0,2]]
        for i in range(0,7,1):
            self.board += [[0,0,0,0,0,0,0,0]]
        self.board += [[12,0,0,0,16,0,0,12]]
    def move(self, player,init_row,init_col,fin_row,fin_col):
        if(player != 10 or player != 0):
            return(False)
        if not(init_row <= 8 or init_row >= 0 or init_col <= 8 or init_col >= 0):
            return(False)
        if not(fin_row <= 8 or fin_row >= 0 or fin_col <= 8 or fin_col >= 0):
            return(False)
        if(player == 0 and self.board[init_row][init_col] > 10):
            return(False)
        if(player == 10 and self.board[init_row][init_col] < 10):
            return(False)

        self.board[fin_row][fin_col] = self.board[init_row][init_col]
        self.board[init_row][init_col] = 0
        return(True)
