my_list = [1, 2, 3]

my_set = (1, 2, 3, 4)

print(my_set)

class Dog():
    
    # Сlass object attribute
    
    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed='Labrador', name='Marley', spots=False)

print(my_dog.name)