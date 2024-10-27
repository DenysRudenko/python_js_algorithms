# Use for, .split(), and if to create a Statement that will print out words that start with 's':
print('Solution: 1')

st = 'Print only the words that start with s in this sentence'

for i in st.split():
    if i.startswith('s'):
        print(i)

print("_" * 12)

# use range() to print all the even numbers from 0 to 10
# one solution
print('Solution: 2')

for i in range(0, 11):
    if i%2 == 0:
        print(i)
    else:
        print("Odd num")

print("_" * 12)

# 2nd solution
for i in range(0, 11, 2):
    print(i)

print("_" * 12)

# Use a lost comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('Solution: 3')

divisible = [x for x in range(0, 51) if x % 3 == 0]
print(divisible)

print("_" * 12)

# Go through the string bellow and if the length of a word is even print 'even'
print('Solution: 4')

st2 = 'Print every word in this sentence that has an even number of letters'
lst = st2.split()

for i in lst:
    if len(i) % 2 == 0:
        print(i)

print("_" * 12)

# Write a program that prints integers from 1 to 100, but for multiples of three print 'Fizz',
# instead of the number, and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'

print('Solution: 5')

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print("_" * 12)


# Use list comprehension to create a list of thee first letters of every word in string below

print('Solution: 6')

st3 = 'Create a list of the first letters of every word in this string'

# for i in st3.split():
#     print(i[0])

result1 = [i[0] for i in st3.split()]

print(result1)
