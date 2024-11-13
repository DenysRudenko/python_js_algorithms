class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    

marley = Dog("Marley")

patrick = Cat("Patrick")

print(marley.speak())
print(patrick.speak())

for pet in [marley, patrick]: 

    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())

pet_speak(patrick)
pet_speak(marley)


class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"
    

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"
    
fido = Dog("Fido")

isis = Cat("Isis")

print(fido.speak())

print(isis.speak())
