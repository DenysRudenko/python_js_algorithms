x = 25

def printer():
    x = 50
    return x

# global
name = 'This is a global string'

def greet():

    #  enclosing
    name = 'Sammy'

    def hello():
        # local
        print('Hello ' + name)

    hello()


greet()

x = 50

def func():

    print(f'X is {x}')

    # local reassignment on a global variable!
    x = 'new value'
    print(f'i just locally changed global X to {x}')
    return x


print(x)
