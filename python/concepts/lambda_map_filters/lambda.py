def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)


print(list(map(square, my_nums)))

def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'Even'
    else:
        return my_string[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0

my_nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, my_nums)))

for n in filter(check_even, my_nums):
    print(n)

square_2 = lambda num: num ** 2
print(square_2(5))

print(list(map(lambda num: num**2, my_nums)))


print(list(filter(lambda num:num % 2 == 0, my_nums)))

print(list(map(lambda name: name[::-1], names)))

def first_letter(string):

    for char in string:
        print(char[::-1])



print(first_letter(['andy', 'denys', 'Patrick']))