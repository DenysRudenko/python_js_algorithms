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
print("-" * 30)


class Human():

    def __init__(self, name, surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height

    def ideal_weight_lorence(self):
        return (self.height - 100) - (self.height - 152) * 0.2

    def __str__(self):
        ideal_weight = self.ideal_weight_lorence()
        weight_difference = self.weight - ideal_weight
        
        return (f'Hello {self.name} {self.surname}, you are {self.age} years old! '
                f'Your weight is {self.weight}kg and your height is {self.height}cm!\n'
                f'Your ideal weight by Lorence formula is {ideal_weight:.2f}kg.\n'
                f'You need to lose {weight_difference:.2f}kg!')
    

alex = Human("Alex", "Kravchenko", 25, 80, 180)

print(alex)

print("-" * 30)

class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calc_area(self):
        return self.width * self.height
    
    def __str__(self):
        return f'The area of rectangle is {self.calc_area()}'
    

new_rectange = Rectangle(200, 100)

print(new_rectange)

