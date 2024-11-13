from typing import List

class Human():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def greeting(self):
        return f"Hi, I am human and my name is {self.name}!"



class Worker(Human):

    def __init__(self, name, surname, age, id, nationality, gender):

        super().__init__(name, surname, age)

        self.id = id
        self.nationality = nationality
        self.gender = gender

    def greeting(self):
        return f"Hi, I am Worker and my name is {self.name}!"


class Developer(Worker):

    def __init__(self, name, surname, age, id, nationality, gender, language, experience):
        super().__init__(name, surname, age, id, nationality, gender)

        self.language = language
        self.experience = experience

    def greeting(self):
        return f"Hi, I am Developer and my name is {self.name}!"
    
    def __str__(self):
        return (
            f"Developer Details:\n"
            f'Name: {self.name} {self.surname}\n'
            f'Age: {self.age}\n'
            f'ID: {self.id}\n'
            f'Nationality: {self.nationality}\n'
            f'Gender: {self.gender}\n'
            f'Programming language: {self.language}\n'
            f'Experience: {self.experience} years'
        )

alex = Developer("Alex", "Doe", "27", 12, "Ukrainian", "Male", "Python", 3)
david = Worker("David", "Karetsky", 15, 1, "Irish", "male")
igor = Human("Igor", "Kushnir", 43)


# print(alex.greeting())
# print(david.greeting())
# print(igor.greeting())

my_list: List[Human] = [alex, david, igor]

for person in my_list:
    print(person.greeting())

