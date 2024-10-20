def my_func(a, b, c=0, d=0,e=0):
    # return 5 percent of the sum of a and b
    return sum((a, b, c , d, e)) * 0.05

print(my_func(40, 60, 100, 100))

def my_func_two(*args):
    return sum(args) * 0.05

print(my_func_two(40, 60, 100))

def my_func_three(*args):
    for item in args:
        print(item)

my_func_three(1, 2, 3, 4 ,5 ,6)


def my_func_four(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")

my_func_four(fruit='orange', meal='pasta')


def test_func(*args, **kwargs):
    print("Positional arguments", args)
    print("Keyword arguments", kwargs)

test_func(1, 2 ,3, name='Denys', age=24, job='student')

def my_func_five(**kwargs):
    print(kwargs)

my_func_five(name = 'Denys', surname='Rudenko', age=24, hair='blondie')


def my_func_six(*args):
    print(args)

my_func_six(1, 2, 3, 6, 10)


def my_func_seven(*args, **kwargs):
    print(args)
    print(kwargs)
    
    print('I would like {} {}'.format(args[2], kwargs['animals']))

my_func_seven(10, 20, 30, fruit='orange', food='eggs', animals='cats')
