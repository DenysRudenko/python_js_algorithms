# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as 4/3pr**3

import math
 
def vol(rad):
    
    r_cube = rad ** 3

    formula = (4 / 3) * math.pi * r_cube

    return formula


print(vol(2))
print('-'* 21)

# Write a function that checks whether
# a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):

    if num in range(low, high + 1):
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is out of bounds!'


print(ran_check(8, 2, 7))
print(ran_check(5, 2, 7))
print('-' * 21)


def run_bool(num, low, high):
    
    if num in range(low, high + 1):
        return True
    else:
        return False


print(run_bool(3, 1, 10))
print(run_bool(11, 1, 10))
print('-' * 21)



