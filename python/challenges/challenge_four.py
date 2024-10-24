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

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

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