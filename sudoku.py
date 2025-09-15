from random import *
from bisect import *
class Sudoku:
    def __init__(self):
        self.board = []
        self.play = [[0 for _ in range(9)] for _ in range(9)]
        self.x = [0, 3, 6]
        self.y = [0, 3, 6]
    def check_row(self, row: int):
        return all(self.play[row][i] == self.board[row][i] for i in range(1, 10))
    def check_col(self, col: int):
        return all(self.play[i][col] == self.board[i][col] for i in range(1, 10))
    # Kiem tra box
    def check_id(self, row: int, col: int):
        return self.play[row][col] == self.board[row][col]
    def check_bigbox(self, row: int, col: int):
        xpos = bisect_left(self.x, row)
        ypos = bisect_left(self.x, col)
        
    def check_board(self):
        return all((self.play[i][j] != 0 and self.play[i][j] == self.board[i][j]) for i in range(9) for j in range(9))
sudoku = Sudoku()
