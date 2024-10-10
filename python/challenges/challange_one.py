import math

exp_one = 4 * (6 + 5)
exp_two = 4 * 6 + 5
exp_three = 4 + 6 * 5

print(exp_one, exp_two, exp_three)

type_exp = 3 + 1.5 + 4

print(type(type_exp))

square_root_num = 16

print(math.sqrt(square_root_num))

square_num = 4 ** 2

print(square_num)

my_string = "Hello"

# Print out 'e' using indexing
print(my_string[1])

# Reverse the string 'hello' using slicing:
print(my_string[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.

print(my_string[-1])
print(my_string[4])

# lists 

# Build this list [0,0,0] two separate ways.
my_list = [0, 0]
my_list.append(0)

print(my_list)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]

list3[2][2] = 'goodbye'

print(list3)

# Sort the list below:

list4 = [5, 3, 4, 6, 1]
print(list4)
list4.sort()
print(list4)

# dictionaries

# # Grab 'hello'
d = {
    'simple_key': 'hello'
}

print(d['simple_key'])

# Grab 'hello'
d = {
    'k1': {
        'k2': 'hello'
    }
}

print(d['k1']['k2'])

# Grab hello
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
# Grab hello
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])

# sets
# Use a set to find the unique values of the list below
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]

list5 = set(list5)

print(list5)