from random import *
from bisect import *
from time import sleep
class Sudoku:
    def __init__(self):
        rand_choice = [(i, j) for i in range(9) for j in range(9)]
        #processing front-end: most important
        self.board = self._generate_full_board()
        # back-end
        self.play = [row.copy() for row in self.board]
        for _ in range(12):
            option = choice(rand_choice)
            i, j = option
            rand_choice.remove(option)
            self.play[i][j] = 0
        self.rows = [0, 3, 6, 9]
        self.cols = [0, 3, 6, 9]
        self.command = ['del', 'w']
    def _generate_full_board(self):
        """Sinh một bảng sudoku hợp lệ."""
        # Cách nhanh: dùng mẫu sudoku chuẩn rồi tráo hàng/cột
        base = 3
        side = base * base

        # Mẫu ban đầu
        def pattern(r: int, c: int): return (base*(r % base)+r//base+c) % side
        # Trộn ngẫu nhiên
        def shuffle(s: list[int]): return sample(s, len(s))

        rBase = range(base)
        rows  = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols  = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums  = shuffle(range(1, side+1))

        return [[nums[pattern(r, c)] for c in cols] for r in rows]
    def check_row(self, row: int):
        return all(self.play[row][i] == self.board[row][i] for i in range(9))
    def check_col(self, col: int):
        return all(self.play[i][col] == self.board[i][col] for i in range(9))
    # Kiem tra box
    def check_id(self, row: int, col: int) -> bool:
        return self.play[row][col] == self.board[row][col]
    def check_bigbox(self, row: int, col: int):
        row_pos = bisect_right(self.rows, row)
        col_pos = bisect_right(self.cols, col)
        return all(self.play[i][j] == self.board[i][j] for i in range(self.rows[row_pos - 1], self.rows[row_pos]) for j in range(self.rows[col_pos - 1], self.rows[col_pos]))
        
    def check_board(self):
        return all((self.play[i][j] != 0 and self.play[i][j] == self.board[i][j]) for i in range(9) for j in range(9))
    def ready_play(self):
        print("Welcome to Sudoku game.")
        print("Set up...")
        sleep(1)
        print("Sync with database...")
        sleep(1)
        print("Almost done...")
        sleep(0.5)
        print("Done.")
        sleep(0.2)
        inp = input("Did you know rules to play?\nType (y/n): ").lower().strip()
        if inp == "y":
            print("Alright, so now let go to addition rules")
            print("There are some boxes that are delete and put the zero.\nAs no sample, plz dont mind")
            print(f"There are some command that you can use during the game, including {self.command} with form:\n \t[command] row column [number to fill]")
            print("If you wanna stop instantly, input 0 to quit")
        elif inp == 'n':
            print("Let go to the main rules (Enter to continue)")
            input("There are columns and rows that are filled with the number from 1 to 9\nFor example (with a rows): [1, 2, 3, 4, 5, 6, 7, 8, 9]")
            input("Then I change RANDOM position into 0 (as this is a small game -> plz dont mind)")
            input("What you have to do is filling those boxes")
            print(f"There are some command that you can use to fill during the game, including {self.command} with form:\n \t[command] row column [number to fill]")
            print("If you wanna stop instantly, input 0 to quit")
        #print(*self.board, sep="\n")
sudoku = Sudoku()
sudoku.ready_play()
