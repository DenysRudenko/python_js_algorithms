def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


# new_input = int(input("Please enter your value: "))

# position_index = input("Choose an index position: ")

# another_input = list(input("please anter a value: "))

# display(new_input, position_index, another_input)


def choice():

    choice = 'WRONG'

    while choice.isdigit() == False:

        choice = input("Please enter a number (0-10): ")

        if choice.isdigit() == False:
            print("Sorry that is not a digit")

    return int(choice)

result = 'Wrong Value'
acceptable_values = [0, 1, 2]

result in acceptable_values

choice()


def user_choice():

    # variables
    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_range = False

    # two conditions to check
    # digit or within range is false

    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): ")

        # digit check
        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        # range check
        if choice.isdigit() == True:
            if choice in acceptable_range:
                within_range = True
            else:
                print("sorry only 0-10")
                within_range = False

    return int(choice)

user_choice()