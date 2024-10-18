x = 50

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print('X is not less than 5')

# break, continue, pass keywords

y = [1, 2, 3]

for item in y:
    # comment
    pass

print('end of my script')


my_string = "Sammy"

for letter in my_string:
    # skipping 'a' char in my_string
    if letter == 'm':
        # continue
        break
    print(letter)

z = 0

while z < 5:
    if z == 2:
        break    
    print(z)
    x += 1

