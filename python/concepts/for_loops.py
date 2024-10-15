my_list = [1, 2 ,3, 4, 6]

for num in my_list:
    print(num)

print('---------------')

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f'our odd numbers is {num}')

list_sum = 0

for num in my_list:
    list_sum += num

print(list_sum)
print('---------------')


my_string = 'hello world'

for letter in my_string:
    print(letter)

print('---------------')

tup = (1, 2, 3)

for item in tup:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6)]

len(mylist)

for item in mylist:
    print(item)

print('---------------')

for a, b in mylist:
    print(a)
    print(b)

print('---------------')

my_new_list = [(1, 2, 3), (4, 5, 6), (7, 8 ,9)]

for a, b, c in my_new_list:
    print(c)

print('---------------')

my_dict = {'k1': 4, 'k2': 2, 'k3': 3}

for value in my_dict.items():
    print(value)

for value in my_dict.values():
    print(value)
