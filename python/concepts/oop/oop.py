my_list = [1, 2, 3]

my_set = (1, 2, 3, 4)

print(my_set)

class Dog():
    
    # Сlass object attribute
    # same for any instance of a class
    species = "mammal"
    
    def __init__(self, breed, name):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print("Woof! My name is {} and the number is {}!".format(self.name, number))

my_dog = Dog("Labrador", "Frankie")

my_dog.bark(10)

print(my_dog.species)


class Circle():
    
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.area = radius * radius * self.pi

    # method 
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)

print(my_circle.pi)

print(my_circle.area)

print(my_circle.get_circumference())
print("-" * 30)


class Triangle():

    def __init__(self, base=3, height=4):
        
        self.base = base
        self.height = height

    def get_area(self):
        return 1/2 * (self.base * self.height)
    

triangle_area = Triangle()

print(triangle_area.get_area())