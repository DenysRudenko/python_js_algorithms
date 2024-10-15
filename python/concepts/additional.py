"""
    This comment,
    which one takes multiple lines

"""

print(1, 2, 3, 4, 5, sep='|')

# name = input('Enter you name:')
# surname = input('Enter your surname:')

# print("Dear " + name + " " + surname + ", welcome to Python course!")

x = -5
y = 10

#  print out the module of number in 'x' variable
print(abs(x))

#  print out a rounded divider, and then modulo from x to y
print(divmod(x, y))

list = [1, 2 ,3 , 4, 5]

print(max(list))
print(min(list))

# f strings

print(f'Y variable = {y}')
print(f'type of y: {type(y)}')

# num = float(input("Please enter a float:"))
# print(num)

# challenge 2 

# weight = float(input("Enter your weight:"))
# height = float(input("Enter your height:"))

# formula = weight / (height ** 2)

# print(f'Your index is: {formula}')

# challenge 3

# number = input("Please enter 4 digit number: ")

# print(number[-2])

# challenge 4

seconds = int(input("Enter your seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
est_seconds = seconds % 60

print(f'{hours} h {minutes} min {est_seconds} s')