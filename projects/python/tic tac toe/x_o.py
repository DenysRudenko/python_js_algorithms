import random

def instructions():
    """
    Tic-Tac-Toe instructions with a basic rules.
    """
    
    print("=" * 70)
    print("|{:^68}|".format(" Welcome to the Tic-Tac-Toe Game! "))
    print("=" * 70)
    print("|{:^68}|".format("1. The game is played on a 3x3 grid, numbered as shown below."))
    print("|{:^68}|".format("2. Players take turns entering their moves                   "))
    print("|{:^68}|".format("3. The first who align X or O in the row, wins the game.     "))
    print("|{:^68}|".format("4. If 3x3 matrix filled out, without a winner, then - draw.  "))
    print("|{:^68}|".format("5. To make a move, enter a number from 1 to 9 when prompted. "))
    print("|{:^68}|".format("6. Once you choose a number, its will insert X or O.         "))
    print("=" * 70)

def start_game():
    """
    Asking if user wants to play.

    """
    choice = ""

    while choice not in ["Y", "N"]:

        choice = input("Would you like to play the game? (Y/N): ").upper()

        if choice not in ["Y", "N"]:
            print("Invalid input! Please choose 'Y' or 'N'!")

    return choice == "Y"


def replay():
    """
    Asking if user want to replay.
    """

    choice = ""

    while choice not in ["Y", "N"]:

        choice = input("Would you like to play again? (Y/N): ").upper()

        if choice not in ["Y", "N"]:
            print("Invalid input! Please choose 'Y' or 'N'!")
    
    return choice == "Y"


def display_board(board):
    """
    Displays 3x3 matrix playground for Tic-Tac-Toe.
    """

    print("-" * 9)
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-" * 9)
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 9)
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("-" * 9)


def choose_turn():
    """
    Using random module generates 1 or 2.
    """

    return "Player 1" if random.randint(1, 2) == 1 else "Player 2"



def player_input(turn):
    """
    This function takes user decision to play with 'X' or 'O',
    once user choose the correct letter, while loop breaks.
    """

    choice = ""
    print(f'{turn} will go first!')

    while choice not in ["X", "O"]:

        choice = input(f"{turn}, please choose 'X' or 'O' to continue: ").upper()

        if choice not in ["X", "O"]:

            print("Invalid input! Please choose 'X' or 'O'!")

    if turn == "Player 1":
        return choice, "O" if choice == "X" else "X"
    else:
        return "O" if choice == "X" else "X", choice


def place_marker(board, marker, position):
    """
    Places a player's marker ('X' or 'O') on the specified position of the board.
    """

    board[position] = marker


def win_check(board, mark):
    """
    Checks all indexes in our board if they meet criteria for a win.
    """

    # horizontal rows
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    
    # vertical rows
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    
    # diagonals
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    
    return False


def space_check(board, position):
    """
    Check if any index in the board is empty.
    """

    return board[position] == " "


def full_board_check(board):
    """
    Checks if any index in the board is empty.
    """

    for i in range(1, 10):

        if board[i] == " ":
            return False
        
    return True


def player_choice(board):
    """
    This function asks to pick an index number to insert X or O.
    """

    choice = ''

    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or not space_check(board, int(choice)):
        choice = input("Choose an index where you want insert your letter (1-9): ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input! Please choose between 1-9!")
        elif not space_check(board, int(choice)):
            print("Position is taken, try different one!")

    return int(choice)

       
instructions()

if start_game():
    while True:

        board = [" "] * 10
        game_on = True
        turn = choose_turn()
        player1_marker, player2_marker = player_input(turn)

        while game_on:
            if turn == "Player 1":
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1_marker, position)

                if win_check(board, player1_marker):
                    display_board(board)
                    print("Congratulations! Player 1 has won the game!")
                    game_on = False
                elif full_board_check(board):
                    print("Oh no! Its a draw!")
                    game_on = False
                else:
                    turn = "Player 2"
            
            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_marker, position)

                if win_check(board, player2_marker):
                    display_board(board)
                    print("Congratulations! Player 2 has won the game!")
                    game_on = False
                elif full_board_check(board):
                    print("Oh no! Its a draw!")
                    game_on = False
                else:
                    turn = "Player 1"

        if not replay():
            print("Thanks for playing!")
            break
else:
    print("Maybe next time, goodbye! :)")

