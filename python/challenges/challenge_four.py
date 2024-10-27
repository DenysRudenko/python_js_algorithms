# Warm up section

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

print(lesser_of_two_evens(2, 4))

print('-' * 20)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    words = text.split()

    for word in words:
        print(f'The first letter of both words is {word[0]}')
        
        if words[0][0]  == words[1][0]:
            return True
        else:
            return False


    return words

print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Cangaroo"))

print('-' * 20)

# MAKES TWENTY: Given two integers, return True if the total_sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1, n2):

    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False
    

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))

print('-' * 20)


# level 1 problems

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a  
# old_macdonald('macdonald') --> MacDonald
# macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    return name[0].upper() + name[1:3]  + name[3].upper() + name[4:]


print(old_macdonald('macdonald'))
print('-' * 20)


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    string = text.split()
    # lst = list(reversed(string))
    string.reverse()

    return " ".join(string)


print(master_yoda("I am home"))
print(master_yoda("We are ready"))
print('-' * 20)


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# abs(num) returns the absolute value of a number

def almost_there(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print('-' * 20)



# Level 2 Problems
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
  
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
        
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 1, 3, 1, 3, 3]))

print('-' * 20)


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
     chars = ''

     for char in text:
         chars += char * 3

     return chars

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

print('-' * 20)


# BLACKJACK: Given three integers between 1 and 11, if their total_sum is less than or equal to 21, return their total_sum. 
# If their total_sum exceeds 21 and there's an eleven, reduce the total total_sum by 10. Finally, if the total_sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def black_jack(a, b, c):
    total_sum = a + b + c

    if total_sum <= 21:
        return total_sum
    elif total_sum > 21 and (a == 11 or b == 11 or c == 11):
        total_sum -= 10

    if total_sum > 21:
        return 'BUST'
    else:
        return total_sum
        
    

print(black_jack(5, 6, 7))
print(black_jack(9, 9, 9))
print(black_jack(9, 9, 11))
print('-' * 20)


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    total = 0
    ignore = False

    for num in arr:
        if num == 6:
            ignore = True
        elif num == 9 and ignore:
            ignore = False
        elif not ignore:
            total += num

    return total


print(summer_69([]))
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print('-' * 21)


# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    lst = [0, 0, 7]

    for num in nums:
        if num == lst[0]:
            lst.pop(0)

        if not lst:
            return True

    return False


print(spy_game([0, 0, 7]))
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print('-' * 21)


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.


def count_primes(num):
    prime_counter = 0

    if num < 2:
        return 0

    for n in range (2, num + 1):
        is_prime = True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_counter += 1



    return prime_counter
  

print(count_primes(100))
print('-' * 21)


# Just for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".


def print_big(letter):
    letter_dict = {
        'A' : [
            "  *  ",
            " * * ",
            "*****",
            "*   *",
            "*   *"
        ],
        'B': [
            "**** ",
            "*   *",
            "**** ",
            "*   *",
            "**** "
        ],
        'C':[
            " ****",
            "*    ",
            "*    ",
            "*    ",
            " ****"
        ],
        'D':[
            "**** ",
            "*   *",
            "*   *",
            "*   *",
            "**** "
        ],
        'E':[
            "*****",
            "*",
            "*****",
            "*",
            "*****"
        ]
    }

    letter_dict = letter_dict.get(letter.upper(), ['Letter not avaliable'])

    for char in letter_dict:
        print(char)



print(print_big('a'))
