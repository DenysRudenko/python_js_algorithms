# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as 4/3pr**3

import math
 
def vol(rad):
    
    r_cube = rad ** 3

    formula = (4 / 3) * math.pi * r_cube

    return formula


print(vol(2))
print('-'* 21)

# Write a function that checks whether
# a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):

    if num in range(low, high + 1):
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is out of bounds!'


print(ran_check(8, 2, 7))
print(ran_check(5, 2, 7))
print('-' * 21)


def run_bool(num, low, high):
    
    return num in range(low, high + 1)


print(run_bool(3, 1, 10))
print(run_bool(11, 1, 10))
print('-' * 21)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()

def up_low(s):
    upper_counter = 0
    lower_counter = 0

    
    for char in s:
        if char.isupper():
            upper_counter += 1
        elif char.islower():
            lower_counter += 1

    message = f'Original String : {s}\nNo. of Upper case Characters : {upper_counter}\nNo. of Lower case Characters : {lower_counter}'
    
    print(message)




s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

print('-' * 21)



# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):

    print(set(lst))


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

print('-' * 21)

# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):

    result = 1

    for num in numbers:
        result *= num
    
    return result

print(multiply([1,2,3,-4]))
print('-' * 21)



# Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
# e.g., madam,kayak,racecar, or a phrase "nurses run".
# Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces.
# Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.


def palindrome(s):
    my_string = ''.join(s.split())

    return my_string == my_string[::-1]
    

print(palindrome("helleh"))
print(palindrome("madam"))
print(palindrome("kayak"))
print(palindrome("racecar"))
print(palindrome("nurses run"))
print(palindrome("hello"))
print(palindrome("cat"))


