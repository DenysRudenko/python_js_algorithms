board = [" "] * 10

def display_board(board):

    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-" * 9)
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 9)
    print(board[7] + " | " + board[8] + " | " + board[9])

display_board(board)

def player_input():

    choice = ""

    while choice not in ["X", "O"]:

        choice = input("Please choose X or O to begin: ").upper()

        if choice not in ["X", "O"] :
            print("Invalid letter! Please choose either X or O.")

    player1_choice = choice
    player2_choice = "O" if player1_choice == "X" else "X"

    print(f"Player 1 choice is: {player1_choice}, player 2 choice is: {player2_choice}")

    return player1_choice, player2_choice


player1_choice, player2_choice = player_input()






