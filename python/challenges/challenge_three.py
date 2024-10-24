# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

def my_func(*args):
    even_num = []

    for arg in args:
        if arg % 2 == 0:
            even_num.append(arg)
    
    return even_num

print(my_func(1, 2, 3, 4, 5, 6, 7, 8, 9))

# Define a function called is_greater that takes in two arguments, and returns True if the first value is greater than the second, False if it is less than or equal to the second.

def is_greater(a, b):
    if a > b:
        return True
    elif a <= b:
        return False
    
print(is_greater(30, 20))

# Define a function called is_even that takes in one argument, and returns True if the passed-in value is even, False if it is not.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(11))

# Define a function called myfunc that takes in two arguments and returns their sum.

def my_func_two(a, b):
    return sum((a, b))

print(my_func_two(2, 2))

print("=" * 6)

# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase,
# and every odd letter is lowercase.
# Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
# The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string

def my_func_three(string):
    result = ''

    for index, letter in enumerate(string):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()

    return result
  
print(my_func_three("Anthropomorphism"))
