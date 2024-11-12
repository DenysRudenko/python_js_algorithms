class Animal():

    def __init__(self):
        print("ANIMAL CREATED!")

    def who_am_i(self):
        print("I am an animal!")

    def eat(self):
        print("I am eating!")

my_animal = Animal()

# print(my_animal.who_am_i())

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def eat(self):
        print("I am a dog and eating!")

    def bark(self):
        print("WOOF!")
    

my_dog = Dog()
my_dog.eat()
my_dog.bark()
