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

