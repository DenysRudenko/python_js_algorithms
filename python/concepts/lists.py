my_list = [1, 2, 3]

my_list = ['String', 100, 23.2]

print(len(my_list))

print(my_list)

print(my_list[1:])

my_second_list = [1, 0, 0.5]

print(my_list + my_second_list)

my_list = my_list.append('six')

print(my_list)

just_list = ['one', 'two', 'three']

# adding new argument
just_list.append('four')

print(just_list)

# getting rid of specific element 
just_list.pop(0)

print(just_list)

string_list = ['a', 'b', 'c', 'd']

num_list = [4, 1, 3, 2]

string_list = num_list

print(string_list)

# sorting the elements by asc order

string_list.sort()

#  reverse the elements 12345 => 54321
num_list.reverse()

print(num_list)

