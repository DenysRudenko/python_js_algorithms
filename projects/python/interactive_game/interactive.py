from IPython.display import clear_output

game_list = [0, 1, 2]
game_on = True

def display_game(game_list):
    print(f"Here is the current list: {game_list}")

def position_choice():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input("Pick a position (0, 1, 2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry invalid choice!")

    return int(choice)

def replacement_choice(game_list, position):

    user_placement = input("Type a string to place a position: ")

    game_list[position] = user_placement

    return game_list

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, I dont understand, please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False

while game_on:
    clear_output()

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()