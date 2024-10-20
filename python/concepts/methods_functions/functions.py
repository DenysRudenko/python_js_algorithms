def name_of_function(name):
    '''
    Docstring explains function
    '''
    print('Hello ' + name)

name_of_function('Denys')

def add_function(num1, num2):
    '''
    adding the arguments
    '''
    return num1 + num2

result = add_function(1, 2)

print(result)

def say_hello():
    '''
    Its just a print function.
    '''
    print("Hello")
    print("How are you?")

say_hello()

def say_hello(name = 'Default'):
    print(f'Hello {name}')

say_hello()

def add_num(num1, num2):
    return num1 + num2

result = add_num(10, 20)

print(result)

def print_result(a, b):
    print(a + b)

def return_result(a, b):
    return a + b

print_result(10, 20)

print(return_result(10, 20))

def my_func(a, b):
    print(a + b)
    return a + b

result = my_func(10, 50)

def sum_numbers(num1, num2):
    return num1 + num2

result = sum_numbers('10', '70')

print(result)