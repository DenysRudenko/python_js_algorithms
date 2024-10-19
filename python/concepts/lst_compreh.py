my_string = "Hello"

my_list = []

for letter in my_string:
    my_list.append(letter)

print(my_list)

my_list2 = [letter for letter in my_string]

print(my_list2)

my_list3 = [x for x in 'word']

print(my_list3)

my_list4 = [num**2 for num in range(0, 11)]

print(my_list4)

my_list5 = [x for x in range(0, 11) if x % 2==0 ]

print(my_list5)

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celcius]

print(fahrenheit)

fahrenheit = []

for temp in celcius:
    fahrenheit.append((9/5) * temp + 32)

print(fahrenheit)

# if else stmt

result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]

print(result)

my_list6 = []

for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        my_list6.append(x*y)

print(my_list6)


my_list7 = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]

print(my_list7)