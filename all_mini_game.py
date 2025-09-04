def guess_number():
        from random import randint

        a = randint(1, 100)
        times = randint(10, 20)

        print(f"Guess the number from 1 to 100\nYou have {times} times to guess")

        try:
                while times > 0:
                        choice = int(input("Guess: "))

                        if choice == a:
                                print("Wow, you are genius!!!")
                                print("Ok, correct.")
                                break
                        times -= 1
                        if choice > a:
                                need = "Greater"
                        else:
                                need = "Smaller"

                        if times > 0:
                                print(f"{need}, try again. You now have {times} times left")
                        else:
                                print("No more chance and wrong guess. Better luck next time.")

        except Exception as e:
                print("ERROR, Exit code: -1")


def rock_paper_scissors():
        from random import choice

        options = ["rock", "paper", "scissors"]

        print("Rock-Paper-Scissors Game!")
        while True:
                user = input("Your choice (rock/paper/scissors or 0 to quit): ").lower()
                if user == "0":
                        print("Bye!")
                        break
                if user not in options:
                        print("Invalid choice!")
                        continue
                comp = choice(options)
                print("Computer:", comp)
                if user == comp:
                        print("Draw!")
                elif (user == "rock" and comp == "scissors") or \
                        (user == "scissors" and comp == "paper") or \
                        (user == "paper" and comp == "rock"):
                        print("You win!")
                else:
                        print("You lose!")


def tic_tac_toe():
        import time, random
        def check_horizontal(board: list[list[str]], collision: str):
                for i in board:
                        if all(j == collision for j in i):
                                return True
                return False
        def check_vertical(board: list[list[str]], collision: str):
                for j in range(len(board[0])):
                        if all(i[j] == collision for i in board):
                                return True
                return False
        def check_diag_l_r(board: list[list[str]], collision: str):
                if (all(board[i][i] == collision for i in range(len(board[0])))):
                        return True
                return False
        def check_diag_r_l(board: list[list[str]], collision: str):
                pairs = list(enumerate([i for i in range(len(board[0]) - 1, -1, -1)]))
                if all(board[i][j] == collision for i, j in pairs):
                        return True
                return False
        def check_win(board: list[list[str]], collision: str):
                return check_horizontal(board, collision) \
                        or check_vertical(board, collision) \
                        or check_diag_l_r(board, collision) \
                        or check_diag_r_l(board, collision)
        
                
        print("TIC-TAC-TOE time...")
        print("Wait for the setup...")
        board = [[" " for _ in range(5)] for _ in range(5)]
        def update(board: list[list[str]], i: int, j: int, filling: str):
                if board[i - 1][j - 1] == " ":
                        board[i - 1][j - 1] = filling
                        return board, True
                return board, False
        time.sleep(0.3)
        print("Default 5x5. Other version is not supported!!!")
        
        user_inp = input("Choose 'X' or 'O': ").strip().upper()
        computer_char = "O" if user_inp == "X" else "X"
        print(f"Rule: The computer will choose one box to fill {computer_char},\nthen you fill by giving the address of the box")
        print("'Delete' function is temporarily not supported.")
        print("'X' go first...")
        go = "X"
        while True:
                if user_inp == go:
                        i, j = map(int, input("Address: ").split())
                        if not (1 <= i <= 5 and 1 <= j <= 5):
                                print("Invalid address! Please enter numbers between 1 and 5.")
                                continue
                        new_board, changed = update(board, i, j, go)
                        if not changed:
                                print("Nothing Changed")
                                continue
                        # Print board
                        board = new_board
                        #print(*board, sep="\n")
                        if check_win(board, go):
                                print("You Win. END")
                                break
                        go = computer_char
                elif computer_char == go:
                        # Computer randomly chooses an empty cell
                        empty_cells = [(row + 1, col + 1) for row in range(5) for col in range(5) if board[row][col] == " "]
                        if not empty_cells:
                                print("Draw! No more moves.")
                                break
                        i, j = random.choice(empty_cells)
                        print(f"Computer chooses: {i} {j}")
                        board, _ = update(board, i, j, go)
                        print(*board, sep="\n")
                        if check_win(board, go):
                                print("Computer Wins. END")
                                break
                        go = user_inp
                        
def hangman():
        import time, random
        word = [
                # Animals
                "elephant", "monkey", "tiger", "dolphin", "python",
                "giraffe", "kangaroo", "penguin", "alligator", "rabbit",
                
                # Fruits / Food
                "banana", "strawberry", "watermelon", "pizza", "sandwich",
                
                # Places
                "vietnam", "japan", "egypt", "canada", "paris",
                
                # Tech / Misc
                "internet", "robot", "galaxy", "satellite", "music"
        ]

        hint = [
                # Animals
                "A giant animal with a trunk and big ears.",
                "An agile animal, mainly living on trees, not a squirrel.",
                "Striped predator, very fast.",
                "It lives in the sea, not as big as a shark.",
                "A programming language named after Monty Python.",
                "The tallest animal with a very long neck.",
                "An animal from Australia that carries its baby in a pouch.",
                "A bird that cannot fly but swims very well.",
                "A reptile similar to a crocodile with a broad snout.",
                "A small hopping animal with long ears.",
                
                # Fruits / Food
                "A yellow fruit that monkeys like.",
                "A red fruit with seeds on the outside.",
                "A large green fruit with juicy red inside.",
                "Italian food with cheese and toppings.",
                "Two slices of bread with filling in between.",
                
                # Places
                "A Southeast Asian country with delicious pho.",
                "Land of sushi and samurai.",
                "Known for pyramids and the Nile River.",
                "Country famous for maple syrup and hockey.",
                "The city of the Eiffel Tower.",
                
                # Tech / Misc
                "The global network connecting computers everywhere.",
                "A machine that can perform tasks automatically.",
                "A massive system of stars and planets.",
                "An object orbiting the Earth or another planet.",
                "Art of organized sounds, melodies, and rhythms."
        ]

        print("Hang-man Time!!!")
        man = ["HEAD", "BODY", "ARM LEFT", "ARM RIGHT", "LEG LEFT", "LEG RIGHT"]
        print(f"You have only {len(man)} times before the game is over.")
        print("SET UP...")
        time.sleep(0.3)
        index = random.randint(0, len(word) - 1)
        print("Game")
        time.sleep(1)
        print("Start")
        print(f"This word have {len(word[index])} letter(s)\nHint: {hint[index]}")
        inp = []
        vocab = word[index]
        choose = list(set(map(str, input("GO\n"))))
        wrong = []
        hung = []
        add_to_hung = 0
        while True:
                for i in choose:
                        if i in vocab:
                                if i in inp:
                                        continue
                                inp.extend(i for _ in range(vocab.count(i)))
                        else:
                                if i in wrong:
                                        continue
                                else:
                                        wrong.append(i)
                                        hung.append(man[add_to_hung])
                                        add_to_hung += 1
                if all((i in inp) for i in vocab):
                        print(f'We have the list of charater is this:\n{inp}')
                        print(f"Sorting the list we have word is: {vocab}. END")
                        break
                if len(hung) == len(man) and len(vocab) != len(inp):
                        print("You lose as the man is full of detail. END")
                        break
                print(f"Now you have {len(man) - len(hung)} times")
                print(f"Man now have {hung}")
                choose = list(set(map(str, input("MORE: "))))
if __name__ == "__main__":
        try:
                while True:
                        print("--- MINI GAME MENU ---")
                        print("1. Guess the Number")
                        print("2. Rock Paper Scissors")
                        print("3. Tic-Tac-Toe")
                        print("4. Hangman")
                        print("0. Quit")

                        choice = input("Choose a game: ")

                        if choice == "1":
                                guess_number()
                        elif choice == "2":
                                rock_paper_scissors()
                        elif choice == "3":
                                tic_tac_toe()
                        elif choice == "4":
                                hangman()
                        elif choice == "0":
                                print("Bye!")
                                break
                        else:
                                print("Invalid choice, try again.")
        except:
                print("ERROR. Exit code: -1")        print("Rock-Paper-Scissors Game!")
        while True:
                user = input("Your choice (rock/paper/scissors or 0 to quit): ").lower()
                if user == "0":
                        print("Bye!")
                        break
                if user not in options:
                        print("Invalid choice!")
                        continue
                comp = choice(options)
                print("Computer:", comp)
                if user == comp:
                        print("Draw!")
                elif (user == "rock" and comp == "scissors") or \
                        (user == "scissors" and comp == "paper") or \
                        (user == "paper" and comp == "rock"):
                        print("You win!")
                else:
                        print("You lose!")


def tic_tac_toe():
        import time, random
        def check_horizontal(board: list[list[str]], collision: str):
                for i in board:
                        if all(j == collision for j in i):
                                return True
                return False
        def check_vertical(board: list[list[str]], collision: str):
                for j in range(len(board[0])):
                        if all(i[j] == collision for i in board):
                                return True
                return False
        def check_diag_l_r(board: list[list[str]], collision: str):
                if (all(board[i][i] == collision for i in range(len(board[0])))):
                        return True
                return False
        def check_diag_r_l(board: list[list[str]], collision: str):
                pairs = list(enumerate([i for i in range(len(board[0]) - 1, -1, -1)]))
                if all(board[i][j] == collision for i, j in pairs):
                        return True
                return False
        def check_win(board: list[list[str]], collision: str):
                return check_horizontal(board, collision) \
                        or check_vertical(board, collision) \
                        or check_diag_l_r(board, collision) \
                        or check_diag_r_l(board, collision)
        
                
        print("TIC-TAC-TOE time...")
        print("Wait for the setup...")
        board = [[" " for _ in range(5)] for _ in range(5)]
        def update(board: list[list[str]], i: int, j: int, filling: str):
                if board[i - 1][j - 1] == " ":
                        board[i - 1][j - 1] = filling
                        return board, True
                return board, False
        time.sleep(0.3)
        print("Default 5x5. Other version is not supported!!!")
        
        user_inp = input("Choose 'X' or 'O': ").strip().upper()
        computer_char = "O" if user_inp == "X" else "X"
        print(f"Rule: The computer will choose one box to fill {computer_char},\nthen you fill by giving the address of the box")
        print("'Delete' function is temporarily not supported.")
        print("'X' go first...")
        go = "X"
        while True:
                if user_inp == go:
                        i, j = map(int, input("Address: ").split())
                        if not (1 <= i <= 5 and 1 <= j <= 5):
                                print("Invalid address! Please enter numbers between 1 and 5.")
                                continue
                        new_board, changed = update(board, i, j, go)
                        if not changed:
                                print("Nothing Changed")
                                continue
                        # Print board
                        board = new_board
                        #print(*board, sep="\n")
                        if check_win(board, go):
                                print("You Win. END")
                                break
                        go = computer_char
                elif computer_char == go:
                        # Computer randomly chooses an empty cell
                        empty_cells = [(row + 1, col + 1) for row in range(5) for col in range(5) if board[row][col] == " "]
                        if not empty_cells:
                                print("Draw! No more moves.")
                                break
                        i, j = random.choice(empty_cells)
                        print(f"Computer chooses: {i} {j}")
                        board, _ = update(board, i, j, go)
                        print(*board, sep="\n")
                        if check_win(board, go):
                                print("Computer Wins. END")
                                break
                        go = user_inp
                        
def hangman():
        import time, random
        word = [
                # Animals
                "elephant", "monkey", "tiger", "dolphin", "python",
                "giraffe", "kangaroo", "penguin", "alligator", "rabbit",
                
                # Fruits / Food
                "banana", "strawberry", "watermelon", "pizza", "sandwich",
                
                # Places
                "vietnam", "japan", "egypt", "canada", "paris",
                
                # Tech / Misc
                "internet", "robot", "galaxy", "satellite", "music"
        ]

        hint = [
                # Animals
                "A giant animal with a trunk and big ears.",
                "An agile animal, mainly living on trees, not a squirrel.",
                "Striped predator, very fast.",
                "It lives in the sea, not as big as a shark.",
                "A programming language named after Monty Python.",
                "The tallest animal with a very long neck.",
                "An animal from Australia that carries its baby in a pouch.",
                "A bird that cannot fly but swims very well.",
                "A reptile similar to a crocodile with a broad snout.",
                "A small hopping animal with long ears.",
                
                # Fruits / Food
                "A yellow fruit that monkeys like.",
                "A red fruit with seeds on the outside.",
                "A large green fruit with juicy red inside.",
                "Italian food with cheese and toppings.",
                "Two slices of bread with filling in between.",
                
                # Places
                "A Southeast Asian country with delicious pho.",
                "Land of sushi and samurai.",
                "Known for pyramids and the Nile River.",
                "Country famous for maple syrup and hockey.",
                "The city of the Eiffel Tower.",
                
                # Tech / Misc
                "The global network connecting computers everywhere.",
                "A machine that can perform tasks automatically.",
                "A massive system of stars and planets.",
                "An object orbiting the Earth or another planet.",
                "Art of organized sounds, melodies, and rhythms."
        ]

        print("Hang-man Time!!!")
        man = ["HEAD", "BODY", "ARM LEFT", "ARM RIGHT", "LEG LEFT", "LEG RIGHT"]
        print(f"You have only {len(man)} times before the game is over.")
        print("SET UP...")
        time.sleep(0.3)
        index = random.randint(0, len(word) - 1)
        print("Game")
        time.sleep(1)
        print("Start")
        print(f"This word have {len(word[index])} letter(s)\nHint: {hint[index]}")
        inp = []
        vocab = word[index]
        choose = list(set(map(str, input("GO\n"))))
        wrong = []
        hung = []
        add_to_hung = 0
        while True:
                for i in choose:
                        if i in vocab:
                                if i in inp:
                                        continue
                                inp.extend(i for _ in range(vocab.count(i)))
                        else:
                                if i in wrong:
                                        continue
                                else:
                                        wrong.append(i)
                                        hung.append(man[add_to_hung])
                                        add_to_hung += 1
                if all((i in vocab) for i in inp):
                        print("END. The word is:", vocab)
                        break
                if len(hung) == len(man) and len(vocab) != len(inp):
                        print("You lose as the man is full of detail. END")
                        break
                print(f"Now you have {len(man) - len(hung)} times")
                print(f"Man now have {hung}")
                choose = list(set(map(str, input("MORE: "))))
if __name__ == "__main__":
        try:
                while True:
                        print("--- MINI GAME MENU ---")
                        print("1. Guess the Number")
                        print("2. Rock Paper Scissors")
                        print("3. Tic-Tac-Toe")
                        print("4. Hangman")
                        print("0. Quit")

                        choice = input("Choose a game: ")

                        if choice == "1":
                                guess_number()
                        elif choice == "2":
                                rock_paper_scissors()
                        elif choice == "3":
                                tic_tac_toe()
                        elif choice == "4":
                                hangman()
                        elif choice == "0":
                                print("Bye!")
                                break
                        else:
                                print("Invalid choice, try again.")
        except:
                print("ERROR. Exit code: -1")
