import random

print("=" * 70)
print("|{:^68}|".format(" Welcome to the Number Guessing Game! "))
print("=" * 70)
print("|{:^68}|".format("Try to guess the number between 1 and 100."))
print("|{:^68}|".format("If your number is within 10 of the target,"))
print("|{:^68}|".format("you'll receive the message 'Warm', otherwise 'Cold'."))
print("|{:^68}|".format("If your guess is closer to the target than your last,"))
print("|{:^68}|".format("you'll receive 'Warmer', otherwise 'Colder'."))
print("|{:^68}|".format("You have 10 chances to guess the number!"))
print("=" * 70)

num = random.randint(1, 100)
chances = 10
guesses = [0]

play = input("Would you like to play? Yes/No: ")

if play.lower() == 'yes' or play.lower() == 'y':

        while True:
            try:
                guess = int(input("Please enter your number: ")) 
            except ValueError:
                print('Invalid input! Please enter a valid number!')
                continue

            # check if the user enter same value
            if guess in guesses:
                print('You already picked that number, choose different one!')
                continue

            # out of bonds checker
            if guess < 1 or guess > 100:
                print('OUT OF BOUNDS!\nTry number between 1 and 100!')
                continue

            # lets check the first guess, and give user tips

            if guesses[-1] == 0:
                if abs(guess - num) <= 10:
                    print('WARM!')
                else:
                    print("COLD!")
            else:
                if abs(guess - num) < abs(guesses[-1] - num):
                    print("WARMER!")
                else:
                    print("COLDER")

            guesses.append(guess)

            chances -= 1
            print(f'You have {chances} chances left!')

            # check the correct number
            if guess == num:
                print(f'Hell yeah! You choose the correct number - {num}.\nIt took you {len(guesses)} moves to guess!')
                break
            
            # we stop the game if user run out of chances
            if chances == 0:
                print(f'Hell no! You are out of chances! The correct number was {num}')

else:
    print('Maybe next time!')
   