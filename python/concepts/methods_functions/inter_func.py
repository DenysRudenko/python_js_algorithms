from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]

def shuffle_list(my_list):
    '''
    This function shuffle the list using shuffle form random
    '''

    shuffle(my_list)
    return my_list

print(shuffle_list(example))

my_hidden_list = [' ', 0, ' ']

print(shuffle_list(my_hidden_list))

def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0, 1, 2: ")

    return int(guess)

print(player_guess())

my_index = player_guess()

def check_guess(my_list, guess):
    if my_list[guess] == '0':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(my_list)


# initial list
my_list = [' ', 0, ' ']

# shuffle list
mixed_up_lst = shuffle_list(my_list)

# user guess
guess = player_guess()

# check guess
print(check_guess(mixed_up_lst, guess))