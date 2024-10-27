# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as 4/3pr**3

import math
 
def vol(rad):
    
    r_cube = rad ** 3

    formula = (4 / 3) * math.pi * r_cube

    return formula


print(vol(2))