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
            self.play[i][j] = '_'
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

        return [[str(nums[pattern(r, c)]) for c in cols] for r in rows]
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
        return all(self.play[i][j] == self.board[i][j] for i in range(self.rows[row_pos - 1], self.rows[row_pos]) for j in range(self.cols[col_pos - 1], self.cols[col_pos]))
    def update(self, board: list[list[str]], i: int, j: int, filling: int):
        if board[i - 1][j - 1] == '_':
            board[i - 1][j - 1] = filling
            return board, True
        return board, False
    def delete(self, board: list[list[str]], i: int, j: int):
        if board[i - 1][j - 1] != self.board[i - 1][j - 1]:
            board[i - 1][j - 1] = 0
            return board, True
        return board, False
    def check_board(self):
        return all(
            self.play[i][j] != '_' and self.play[i][j] == self.board[i][j]
            for i in range(9) for j in range(9)
        )
    def show(self):
        for i in self.play:
            print(*i, sep='  ')
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
            print(f"There are some command that you can use during the game\nIncluding {self.command} with form:\n\t[w] row column [number to fill]\n\t[del] row column")
            print("If you wanna stop instantly, input 0 to quit")
        elif inp == 'n':
            print("Let go to the main rules (Enter to continue)")
            input("There are columns and rows that are filled with the number from 1 to 9\nFor example (with a rows): [1, 2, 3, 4, 5, 6, 7, 8, 9]")
            input("Then computers delete RANDOM position")
            input("What you have to do is filling those boxes")
            print(f"There are some command that you can use to fill during the game\nIncluding {self.command} with form:\n\t[w] row column [number to fill]\n\t[del] row column")
            print("If you wanna stop instantly, input 0 to quit")
        sleep(2)
        print("Ok, let's start.")
        print("Board: ")
        self.show()
        while not self.check_board():
            inp = input("Input: ")
            if inp == "0":
                print("Quit. Bye!")
                return None
            ls_cmd = inp.split()
            command = ls_cmd[0].lower(); r, c = map(int, ls_cmd[1:3]); filling = ls_cmd[3]
            if command == "w":
                new_b, check = self.update(self.play, r, c, filling)
                if not check:
                    print("Nothing changed.")
                    continue
                if self.check_id(r - 1, c - 1):
                    print("Correct.")
                    if self.check_row(r - 1):
                        print("One (more) row completed")
                    if self.check_col(c - 1):
                        print("One (more) column completed")
                    if self.check_bigbox(r - 1, c - 1):
                        print("One (more) box 3x3 completed")
                    
                elif not self.check_id(r, c):
                    print("Wrong.")
                print("Now, the board is:")
                self.show()
                self.play = [row.copy() for row in new_b]
            elif command == "del":
                new_b, check = self.delete(self.play, r, c)
                if not check:
                    print("You cannot delete this box as the box can be correct or fixed")
                    continue
                print("Now, the board is:")
                print(*new_b, sep="\n")
                self.play = [row.copy() for row in new_b]
        else: print("All done. You are genius. END.")
if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.ready_play()
