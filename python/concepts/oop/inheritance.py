class Human():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_fullname(self):
        return f'The fullname is {self.name} {self.surname}!'



class Worker(Human):

    def __init__(self, name, surname, age, id, nationality, gender):

        super().__init__(name, surname, age)

        self.id = id
        self.nationality = nationality
        self.gender = gender


class Developer(Worker):

    def __init__(self, name, surname, age, id, nationality, gender, language, experience):
        super().__init__(name, surname, age, id, nationality, gender)

        self.language = language
        self.experience = experience

    
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

print(alex)

print(alex.get_fullname())


